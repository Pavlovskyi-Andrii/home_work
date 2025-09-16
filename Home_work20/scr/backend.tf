terraform {
  backend "s3" {
    bucket                  = "andrey-s3-bucket-dev"
    key                     = "web/hw20.tfstate"
    region                  = "eu-central-1"
    encrypt                 = true
    skip_credentials_validation = true
    skip_metadata_api_check = true
  }
}
