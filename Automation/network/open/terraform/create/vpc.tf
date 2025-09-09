# Configure Terraform to find the right required_providers

terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.0"
        }
    }
}

# Configure the aws Providers

provider "aws" {
    region = "eu-west-3"
}
