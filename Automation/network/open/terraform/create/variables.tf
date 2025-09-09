variable "vpc_id" {
    type = string
    description = "The id of the vpc_id."
    sensitive = true

    validation {
        condition = length(var.vpc_id) > 4 && substr(var.vpc_id, 0, 4) == "vpc-"
        error_message = "The vpc_id must be a valid VPC id, starting with \"vpc-\"."
    }

}


