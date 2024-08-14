module "iam_deployment" {
  source                  = "./modules/iam"
  role_name               = var.role_name
}


module "lambda_deployment" {
  source                  = "./modules/lambda"
  role                    = module.iam_deployment.role      
  prefix_name             = var.prefix_name	
  lambda_function_name    = var.lambda_function_name
  environment             = var.environment
  tags_conf               = var.tags_conf
  source_file             = var.source_file
  file_type               = var.file_type
  output_file             = var.output_file
  event_handler           = var.event_handler
  lambda_runtime          = var.lambda_runtime
  role_name               = var.role_name
  notebook_instance       = var.notebook_instance
  layer1                  = var.layer1
  layer2                  = var.layer2
}
