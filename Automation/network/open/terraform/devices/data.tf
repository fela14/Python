data "iosxe_rest" "full_config" {
    path = "/data/Cisco-IOS-XE-native:native"
}

output "response" {
    value = data.iosxe_rest.full_config
}

