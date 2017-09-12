from autoprotocol.protocol import Protocol
import json

p = Protocol()
test_plate= p.ref("test_plate", None, "96-pcr", storage="ambient")

def x_seal(protocol, temperature, duration):
    protocol.instructions[-1].data["x_temperature"] = temperature
    protocol.instructions[-1].data["x_duration"] = duration

p.seal(test_plate)
p.unseal(test_plate)

print (json.dumps(p.as_dict(), indent=2))


