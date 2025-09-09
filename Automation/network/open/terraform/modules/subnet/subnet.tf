variable "vpc_id" {}
variable "vpc_cidr_block" {}

resource "aws_subnet" "my_subnet" {
  vpc_id     = var.vpc_id
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = "my-subnet"
  }
}

output "id" {
  value = aws_subnet.my_subnet.id
}
