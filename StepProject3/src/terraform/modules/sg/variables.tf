variable "vpc_id" {
  description = "VPC ID for security group"
  type        = string
}


variable "nat_gateway_id" {
  type    = string
  default = null
}
variable "public_subnet_id" {
  type = string
}
variable "private_subnet_id" {
  description = "ID приватной подсети"
  type        = string
}
