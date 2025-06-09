provider "aws" {
  region = "eu-central-1"
}

# 1. Создание VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# 2. Публичная подсеть
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "eu-central-1a"
  tags = {
    Name = "Andrey_PublicSubnet"
  }
}

# 2.1 Elastic IP для NAT Gateway


resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public.id 
  tags = {
    Name = "NAT Gateway"
  }
}


resource "aws_eip" "nat_eip" {
  domain = "vpc"
}

# 3. Приватная подсеть
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "eu-central-1a"
  tags = {
    Name = "Andrey_PrivateSubnet"
  }
}

# 4. Интернет-шлюз
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}

# 5. Таблица маршрутов для интернета
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

resource "aws_route_table_association" "public_subnet" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# 5.1 Таблица маршрутов для приватной подсети
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }
}

# Привязка route table к приватной подсети
resource "aws_route_table_association" "private_subnet" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# # 6. SSH ключ
# resource "tls_private_key" "example" {
#   algorithm = "RSA"
#   rsa_bits  = 4096
# }

# resource "aws_key_pair" "deployer" {
#   key_name   = "terraform-key"
#   public_key = tls_private_key.example.public_key_openssh
# }

# output "private_key" {
#   value     = tls_private_key.example.private_key_pem
#   sensitive = true
# }

# 7. Security Group (для публичной машины)
resource "aws_security_group" "public_sg" {
  name        = "public_sg"
  description = "Allow SSH from the world"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Разрешаем всем
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 8. Security Group (для приватной машины)
resource "aws_security_group" "private_sg" {
  name        = "private_sg"
  description = "Allow SSH only from public instance"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.public_sg.id] # Только с public SG
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 9. Получаем последнюю Ubuntu 22.04 AMI для eu-central-1
data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# 10. EC2 с публичным IP
resource "aws_instance" "public_ec2" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.public_sg.id]
  key_name                    = "Andrey_05.06"
  associate_public_ip_address = true

  tags = {
    Name = "PublicInstance"
  }
}

# 11. EC2 без публичного IP (приватная)
resource "aws_instance" "private_ec2" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.private.id
  vpc_security_group_ids      = [aws_security_group.private_sg.id]
  key_name                    = "Andrey_05.06"
  associate_public_ip_address = false

  tags = {
    Name = "PrivateInstance"
  }
}
