variable "cidr" {
  type = map(string)

  default = {
    default = "10.0.0.0/24" # fallback for default workspace
    A       = "192.51.100.0/24"
    B       = "203.0.113.0/24"
  }
}

# Create a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = var.cidr[terraform.workspace]

  tags = {
    Name = "workspace-${terraform.workspace}-vpc"
  }
}

# Create two Subnets
resource "aws_subnet" "my_subnet" {
  count      = 2
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = cidrsubnet(aws_vpc.my_vpc.cidr_block, 1, count.index)

  tags = {
    Name = "workspace-${terraform.workspace}-subnet-${count.index}"
  }
}
