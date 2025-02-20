variable "role" {
  type = string
 
}


variable "event_handler" {
  type = string
 
}

variable "lambda_runtime" {
  type = string
 
}

variable "source_file" {
  type = string
   
}

variable "file_type" {
  type = string
}

variable "output_file" {
  type = string
}

variable "prefix_name" {
  type = string  
}

variable "environment" {
  type = string
}

variable "lambda_function_name" {
  type = string
  
} 


variable "layer1" {
  type = string
}

variable "layer2" {
  type = string
}


#####Tags
variable "tags_conf" {
  type = map(string)
}

variable "role_name" {
  type = string
}

####lambda environment variables
variable "notebook_instance" {
  type = string
}




