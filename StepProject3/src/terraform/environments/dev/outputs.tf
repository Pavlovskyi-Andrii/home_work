output "jenkins_master_public_ip" {
  value = module.ec2.jenkins_master_public_ip
}

output "jenkins_worker_private_ip" {
  value = module.ec2.jenkins_worker_private_ip
}
