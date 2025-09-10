resource "iosxe_rest" "snmp_example_chassis_id" {
  method  = "PUT"
  path    = "/data/Cisco-IOS-XE-native:native/snmp-server/chassis-id"
  payload = jsonencode(
    {
      "Cisco-IOS-XE-snmp:chassis-id" = "a_new_chassis_id"
    }
  )
}
