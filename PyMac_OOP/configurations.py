pipelines = ["datapipeline", "lambdapipeline", "containerpipeline", "workflowpipeline", "monitoringpipeline"]

pipeline_var = {
    "datapipeline": [
        {"s3_variables": ["bucket_name", "landing_bucket_id"]},
        {"glue_variables": ["glue_landing_crawler_name", "glue_landing_catalog_name", "glue_landing_catalog_name",
                            "glue_process_job_name", "glue_script_bucket_id"]}
    ],

    "lambdapipeline": [
        {"lambda_variables": ["zip_location", "event_handler", "lambda_runtime", "source_file", "file_type",
                              "output_file", "lambda_function_name"]},
        {"lambda_environment_variables": ["lambda_env", "lambda_host", "lambda_receiver", "lambda_sender",
                                          "sns_arn", "subnet_ids", "security_group_ids"]}
    ],

    "containerpipeline": [
        {"task_definition_variables": ["execution_role", "network_mode", "cpu", "memory", "requires_compatibilities",
                                       "image", "secrets_manager_arn"]},
        {"environment_configuration": ["function_name"]}
    ],

    "workflowpipeline": [
        {"eventbridge": ["schedule_expression", "description", "function_name", "rule", "arn", "is_enabled"]},

        {"stepfunction": ["sf_function_name"]}
    ],

    "monitoringpipeline": [
        {"source_script": ["file_type1", "source_file1", "output_file1"]},
        {"lambda_variables": ["statement_id", "lambda_function_name", "event_handler", "lambda_runtime", "action",
                              "principal"]},
        {"sns_subscription": ["sns_name"]},
        {"email_configuration": ["lambda_host", "lambda_sender", "lambda_receiver", "subnet_id", "security_groups_ids",
                                 "sns_arn", "sns_arn_failed"]},
    ],

}