variable "region" {
  default = "eu-central-1"
}

variable "instance_count" {
  default = 2
}

variable "ami_id" {
  description = "Ubuntu AMI ID"
  type        = string
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Your AWS key pair name"
  type        = string
}

variable "private_key_path" {
  description = "Path to your private SSH key"
  type        = string
}

variable "vpc_id" {
  type = string
}

variable "subnet_id" {
  type = string
}
