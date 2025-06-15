resource "aws_security_group" "nginx_sg" {
  name   = "nginx-sg"
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.list_of_open_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "nginx-sg"
  }
}

resource "aws_instance" "nginx" {
  ami           = "ami-02b7d5b1e55a7b5f1" # Ubuntu 22.04
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.nginx_sg.id]

  associate_public_ip_address = true
  subnet_id = aws_subnet.andrey_sybnet.id 

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install -y nginx
              sudo systemctl start nginx
              sudo systemctl enable nginx
              EOF

  tags = {
    Name = "nginx-instance"
  }
}

resource "aws_subnet" "andrey_sybnet" {
  vpc_id     = var.vpc_id
  cidr_block = "10.0.1.0/24" 
}