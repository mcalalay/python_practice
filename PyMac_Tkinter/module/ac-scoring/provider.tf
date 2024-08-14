provider "aws" {
  region     = var.aws_region
  shared_credentials_file = "%USERPROFILE%/.aws/credentials"
 # profile    = "default"

  #assume_role {
  #role_arn     = "arn:aws:iam::${var.aws_account_id}:role/${var.role_name}"
  #}
	
}