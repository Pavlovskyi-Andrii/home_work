terraform {
  backend "s3" {
    bucket = "terraform-state-danit-devops-8"
    key    = "Andrey/terraform.tfstate"
    region = "eu-central-1"
  }
}
