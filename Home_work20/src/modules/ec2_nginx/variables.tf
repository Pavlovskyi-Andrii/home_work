variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
}

variable "list_of_open_ports" {
  description = "List of ports to open to the world"
  type        = list(number)
}
