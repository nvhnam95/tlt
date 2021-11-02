module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "phutuntlt"
  cidr = "100.129.0.0/21"

  azs             = ["ap-southeast-1a", "ap-southeast-1b", "ap-southeast-1c"]
  private_subnets = ["100.129.0.0/24", "100.129.1.0/24", "100.129.2.0/24"]
  public_subnets  = ["100.129.3.0/24", "100.129.4.0/24", "100.129.5.0/24"]

  enable_nat_gateway   = false
  enable_dns_hostnames = true
#  single_nat_gateway   = true

  tags = {
    Environment = "prod"
    Terraform   = "true"
    Owner       = "infra"
  }
}
