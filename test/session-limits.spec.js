var _ = require('underscore');
var Promise = require('bluebird');
var util = require('util');
var cassandra = Promise.promisifyAll(require('../index'));
var expect = require('chai').expect;
var TestClient = require('./test-client');
var test_utils = require('./test-utils');

var table = 'test_table';
var fields = {
    'row': 'varchar',
    'col': 'int',
    'val': 'int'
};

var key = 'row, col';
var data = test_utils.generate(100000);
var client;

describe('session request limits', function() {
    this.timeout(30000);
    var messages = [];
    function log_callback(err, log) {
        console.log(log.severity, log.message);
        messages.push(log);
    }

    function reset() {
        while(messages.length > 0) {
            messages.pop();
        }
    }

    before(function() {
        cassandra.set_log_callback(log_callback);
        cassandra.set_log_level('INFO');
        client = new TestClient();
        return test_utils.setup_environment(client)
            .then(function() {
                return client.createTable(table, fields, key);
            });
    });

    after(function() {
        return client.cleanup();
    });

    it('inserts a bunch of data', function() {
        return client.insertRowsPreparedBatch(table, data, {});
    });


    function query(opts) {
        var c = new cassandra.Client(opts);
        return c.connectAsync({address: '127.0.0.1'})
        .delay(250) // let logs be emitted
        .then(function() {
            var n = 500;
            return Promise.map(_.range(n), function(i) {
                var cql = util.format('SELECT * from %s.%s', test_utils.ks, table);
                return c.executeAsync(cql, [], {})
                .then(function(result) {
                    return {success: true, result: result};
                })
                .catch(function(err) {
                    return {success: false, result: err.message};
                });
            }, {concurrency: n});
        });
    }

    it('can query with big enough queue settings', function() {
        var opts = {
            core_connections_per_host: 1,
            max_connections_per_host: 1,
            pending_requests_high_water_mark: 16000,
            pending_requests_low_water_mark: 16000
        };

        return query(opts)
        .then(function(result) {
            var errs = _.uniq(_.pluck(_.where(result, {success: false}), 'result'));
            expect(errs.length).equal(0);
        })
    });

    it('reports session errors: queue size limit exceeded', function() {
        var opts = {
            core_connections_per_host: 1,
            max_connections_per_host: 1,
            queue_size_io: 4,
            pending_requests_high_water_mark: 16000,
            pending_requests_low_water_mark: 16000
        };

        return query(opts)
        .then(function(result) {
            var errs = _.uniq(_.pluck(_.where(result, {success: false}), 'result')).sort();
            expect(errs.length).equal(2);
            console.log(errs);
            expect(errs[0]).match(/0 unavailable/);
            expect(errs[0]).match(/1 full queue/);
            expect(errs[1]).match(/The request queue has reached capacity/);
        })
    });

    it('reports session errors: pending request limit exceeded', function() {
        var opts = {
            core_connections_per_host: 1,
            max_connections_per_host: 1,
            pending_requests_high_water_mark: 2,
            pending_requests_low_water_mark: 2
        };

        return query(opts)
        .then(function(result) {
            var errs = _.uniq(_.pluck(_.where(result, {success: false}), 'result'));
            expect(errs.length).equal(1);
            expect(errs[0]).match(/1 unavailable/);
            expect(errs[0]).match(/0 full queue/);
        })
    });
});