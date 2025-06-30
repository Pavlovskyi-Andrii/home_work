resource "aws_instance" "jenkins_master" {
  ami                         = "ami-02003f9f0fde924ea" # Canonical, Ubuntu, 24.04, amd64
  subnet_id                   = var.public_subnet_id
  vpc_security_group_ids      = [var.security_group_id]
  associate_public_ip_address = true
  key_name                    = var.key_name
  instance_type               = var.instance_type
  tags = {
    Name = "Jenkins-Master"
  }
}

resource "aws_spot_instance_request" "jenkins_worker" {
  spot_price    = "0.03" 
  instance_type = "t3.medium"
  ami                    = "ami-02003f9f0fde924ea" 
  subnet_id              = var.private_subnet_id
  vpc_security_group_ids = [var.security_group_id]
  key_name               = var.key_name
  wait_for_fulfillment   = true
  spot_type              = "persistent"


  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y
              apt-get install -y openjdk-17-jre-headless
              mkdir -p /opt/jenkins
              chown ubuntu:ubuntu /opt/jenkins
              EOF



  tags = {
    Name = "Jenkins-Worker"
  }
}
