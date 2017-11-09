from autoprotocol.protocol import Protocol
import json

p = Protocol()
test_plate = p.ref("test_plate", None, "6-flat", storage="ambient")

p.image_plate(test_plate, mode="top", dataref="foo-run")
print (json.dumps(p.as_dict(), indent=2))
