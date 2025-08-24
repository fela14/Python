import main_pb2
import main_pb2_grpc

# Create a RouterRequest
req = main_pb2.RouterRequest(id=1)

# Create a Router with interfaces
router = main_pb2.Router(
    id=1,
    hostname="core-router",
    interfaces=[
        main_pb2.Interface(id=10, description="GigabitEthernet0/0"),
        main_pb2.Interface(id=11, description="GigabitEthernet0/1")
    ]
)

iface4 = router.interfaces.add()
iface4.id = 12
iface4.description = "GigabitEthernet1/0"

iface5 = router.interfaces.add()
iface5.id = 13
iface5.description = "GigabitEthernet1/1"

print(router)

router_bytes = router.SerializeToString()
print(router_bytes)

# Write to file
with open("serialized.bin", "wb") as f:
    f.write(router_bytes)

import binascii
print(binascii.hexlify(router_bytes))

from google.protobuf.json_format import MessageToJson
print(MessageToJson(router))
