module "vpc" {
  source = "../../modules/vpc"

  vpc_cidr_block = var.vpc_cidr_block
  public_subnet_cidr  = var.public_subnet_cidr
  private_subnet_cidr = var.private_subnet_cidr
}

module "sg" {
  source          = "../../modules/sg"
  vpc_id          = module.vpc.vpc_id
  public_subnet_id  = module.vpc.public_subnet_id
  private_subnet_id = module.vpc.private_subnet_id
}


module "ec2" {
  source = "../../modules/ec2"

  vpc_id             = module.vpc.vpc_id
  public_subnet_id   = module.vpc.public_subnet_id
  private_subnet_id  = module.vpc.private_subnet_id
  security_group_id  = module.sg.security_group_id
  key_name           = var.key_name
  instance_type = "t2.micro"
}

