#!/bin/bash

# Отримаємо список IP із Terraform
IPS=$(terraform output -json instance_ips | jq -r '.[]')

echo "[ec2_instances]"
for ip in $IPS; do
  echo "$ip ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/your-key.pem"
done
