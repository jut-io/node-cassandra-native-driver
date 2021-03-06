{
  "target_defaults": {
    "cflags": [ "-Wno-unused-local-typedefs" ]
  },
  "targets": [
    {
        "target_name": "cassandra-native-driver",

        "xcode_settings": {
            "OTHER_CFLAGS": ["-Wno-unused-local-typedefs"]
        },

        "sources": [
        "src/async-future.cc",
        "src/batch.cc",
        "src/cassandra-driver.cc",
        "src/client.cc",
        "src/logging.cc",
        "src/prepared-query.cc",
        "src/result.cc",
        "src/query.cc",
        "src/type-mapper.cc",

        "cpp-driver/src/address.cpp",
        "cpp-driver/src/auth.cpp",
        "cpp-driver/src/auth_requests.cpp",
        "cpp-driver/src/auth_responses.cpp",
        "cpp-driver/src/batch_request.cpp",
        "cpp-driver/src/buffer.cpp",
        "cpp-driver/src/buffer_collection.cpp",
        "cpp-driver/src/cluster.cpp",
        "cpp-driver/src/cluster_metadata.cpp",
        "cpp-driver/src/collection_iterator.cpp",
        "cpp-driver/src/common.cpp",
        "cpp-driver/src/connection.cpp",
        "cpp-driver/src/control_connection.cpp",
        "cpp-driver/src/dc_aware_policy.cpp",
        "cpp-driver/src/error_response.cpp",
        "cpp-driver/src/event_response.cpp",
        "cpp-driver/src/execute_request.cpp",
        "cpp-driver/src/future.cpp",
        "cpp-driver/src/get_time.cpp",
        "cpp-driver/src/handler.cpp",
        "cpp-driver/src/host.cpp",
        "cpp-driver/src/io_worker.cpp",
        "cpp-driver/src/iterator.cpp",
        "cpp-driver/src/latency_aware_policy.cpp",
        "cpp-driver/src/logger.cpp",
        "cpp-driver/src/map_iterator.cpp",
        "cpp-driver/src/md5.cpp",
        "cpp-driver/src/multiple_request_handler.cpp",
        "cpp-driver/src/murmur3.cpp",
        "cpp-driver/src/pool.cpp",
        "cpp-driver/src/prepare_handler.cpp",
        "cpp-driver/src/prepare_request.cpp",
        "cpp-driver/src/prepared.cpp",
        "cpp-driver/src/query_request.cpp",
        "cpp-driver/src/register_request.cpp",
        "cpp-driver/src/replication_strategy.cpp",
        "cpp-driver/src/request_handler.cpp",
        "cpp-driver/src/response.cpp",
        "cpp-driver/src/result_metadata.cpp",
        "cpp-driver/src/result_response.cpp",
        "cpp-driver/src/ring_buffer.cpp",
        "cpp-driver/src/row.cpp",
        "cpp-driver/src/schema_change_handler.cpp",
        "cpp-driver/src/schema_metadata.cpp",
        "cpp-driver/src/session.cpp",
        "cpp-driver/src/set_keyspace_handler.cpp",
        "cpp-driver/src/ssl.cpp",
        "cpp-driver/src/startup_request.cpp",
        "cpp-driver/src/statement.cpp",
        "cpp-driver/src/string_ref.cpp",
        "cpp-driver/src/supported_response.cpp",
        "cpp-driver/src/testing.cpp",
        "cpp-driver/src/token_aware_policy.cpp",
        "cpp-driver/src/token_map.cpp",
        "cpp-driver/src/type_parser.cpp",
        "cpp-driver/src/types.cpp",
        "cpp-driver/src/uuids.cpp",
        "cpp-driver/src/value.cpp",
        "cpp-driver/src/third_party/hdr_histogram/hdr_histogram.cpp"
      ],
      "include_dirs": [
            "<!(node -e \"require('nan')\")",
            "cpp-driver/include",
            "cpp-driver/src/third_party/boost",
            "cpp-driver/src/third_party/rapidjson"
      ]
    }
  ]
}
