/*
# Create a new VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "192.0.2.0/24"
}

# Create subnets using cidrsubnet()
resource "aws_subnet" "my_subnet_1" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "192.0.2.0/25"
}

resource "aws_subnet" "my_subnet_2" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = cidrsubnet("192.0.2.0/24", 1, 1)
}

resource "aws_subnet" "my_subnet_3" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = cidrsubnet(aws_vpc.my_vpc.cidr_block, 2, 0)
}

# Create multiple subnets with count
resource "aws_subnet" "my_subnets" {
  count      = 2
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = cidrsubnet(aws_vpc.my_vpc.cidr_block, 3, count.index)
}

# Create two subnets using cidrsubnet()
resource "aws_subnet" "my_two_subnets" {
  count      = 2
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = cidrsubnet(aws_vpc.my_vpc.cidr_block, 4, count.index)
}
*/
