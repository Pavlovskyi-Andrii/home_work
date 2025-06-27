terraform {
  backend "s3" {
    bucket = "andrey-s3-bucket-dev"     
    key    = "dev/terraform.tfstate"
    region = "eu-central-1"
  }
}
