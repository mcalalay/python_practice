####Provider Variables
aws_region = "us-east-1"


###Lambda Variables

event_handler           = "lambda_function.lambda_handler"
lambda_runtime          = "python3.7"
source_file             = "src/lambda_function.py"
file_type               = "zip"
output_file             = "output/lambda_function_output.zip"
lambda_function_name    = "ac-scoring-sagemaker-launch-handler-v2"
layer1                  = ####
layer2                  = ###


#####Environment Configuration
environment 		        = "prod"
prefix_name 		        = "opsnav-110"
role_name 		            = "Opsnav-client110-developer"



#####Tags
tags_conf = {
Owner  				 = ###
Purpose 		 	 = ####
}

#####Lambda Environment Variables
notebook_instance   = ####