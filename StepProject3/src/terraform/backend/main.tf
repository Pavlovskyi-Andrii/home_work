resource "aws_s3_bucket" "andrey_s3_bucket" {
  bucket = "andrey-s3-bucket-dev"

  tags = {
    Name        = "andrey bucket"
    Environment = "Dev"
  }
}
