output "vpc_id" {
  description = "The VPC ID of Prod env"
  value       = module.vpc.vpc_id
}

output "vpc_private_subnet_ids" {
  description = "List of IDs private subnets of Prod env"
  value       = module.vpc.private_subnets
}

output "vpc_public_subnet_ids" {
  description = "List of IDs public subnets of Prod env"
  value       = module.vpc.public_subnets
}

output "vpc_cidr" {
  description = "CIDR block of VPC"
  value       = module.vpc.vpc_cidr_block
}
output "vpc_private_subnets_cidr_blocks" {
  description = "CIDR blocks of private subnets"
  value       = module.vpc.private_subnets_cidr_blocks
}
output "vpc_public_subnets_cidr_blocks" {
  description = "CIDR blocks of public subnets"
  value       = module.vpc.public_subnets_cidr_blocks
}

output "vpc_nat_public_ips" {
  description = "List of public Elastic IPs created for AWS NAT Gateway"
  value       = module.vpc.nat_public_ips
}

output "azs_private_subnet_ids" {
  value = zipmap(
    module.vpc.azs,
    coalescelist(slice(module.vpc.private_subnets, 0, 3)),
  )
  description = "Map of AZ names to subnet IDs"
}
