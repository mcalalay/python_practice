locals {
    
    func_name	           = "${var.prefix_name}-${var.lambda_function_name}-${var.environment}"
    lambda_arn           = "arn:aws:lambda:${var.aws_region}:${var.aws_account_id}:function:${var.prefix_name}-${var.lambda_function_name}-${var.environment}"

}

data "archive_file" "lambda_1" {
  type        = var.file_type
  source_dir  = var.source_file
  output_path = var.output_file
}

resource "aws_lambda_function" "lambda_func1" {
  filename          = "${var.output_file}"
  function_name     = local.func_name
  role              = var.role
  handler           = var.event_handler
  tags 			        = var.tags_conf
  source_code_hash  = filebase64sha256("${var.output_file}")
  runtime           = var.lambda_runtime
  environment {
    variables = {
      NOTEBOOK_INSTANCE_NAME = var.notebook_instance
    }
  }
  

}