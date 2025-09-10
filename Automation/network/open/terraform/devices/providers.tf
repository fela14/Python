terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = "0.1.1"
    }
  }
}

provider "iosxe" {
  host             = "10.10.20.48"
  device_username  = "developer"
  device_password  = "C1sco12345"
}