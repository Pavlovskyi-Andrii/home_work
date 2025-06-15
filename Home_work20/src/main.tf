provider "aws" {
  region = "eu-central-1"
}



# terraform {
#   backend "s3" {
#     bucket = "terraform-state-danit-devops-8"
#     key    = "Andrey/terraform.tfstate"  
#     region = "eu-central-1"
#   }
# }


module "nginx_instance" {
  source            = "./modules/ec2_nginx"
  vpc_id            = aws_vpc.andrey-vpc.id
  list_of_open_ports = [22, 80]
}


resource "aws_subnet" "andrey_sybnet" {
  vpc_id     = aws_vpc.andrey-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "andrey_sybnet"
  }
}


resource "aws_internet_gateway" "andrey_gw" {
  vpc_id = aws_vpc.andrey-vpc.id

  tags = {
    Name = "andrey_gw"
  }
}

