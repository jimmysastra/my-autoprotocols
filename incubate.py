from autoprotocol.protocol import Protocol
import json

p = Protocol()
src_plate= p.ref("src_plate", None, "96-flat", discard=True)

p.cover(src_plate);
p.incubate(src_plate, "warm_37", "1:minute", shaking=False)


print (json.dumps(p.as_dict(), indent=2))
