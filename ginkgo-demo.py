from autoprotocol.protocol import Protocol
import json

p = Protocol()
gg_plate = p.ref("gg_plate", None, "384-flat", storage="ambient")
tx_plate = p.ref("tx_plate", None, "384-flat", storage="ambient")

p.absorbance(gg_plate, gg_plate.all_wells(),
             "475:nanometer", "tx_absorbance", flashes=1)
p.image_plate(tx_plate, mode="top", dataref="tx_image_ng")
p.transfer(source=tx_plate.well("E19"),
           dest=tx_plate.well("K12"),
           volume="80:microliter")
p.image_plate(tx_plate, mode="top", dataref="tx_image_good")

p.absorbance(tx_plate, tx_plate.all_wells(),
             "475:nanometer", "gg_absorbance", flashes=10)

print (json.dumps(p.as_dict(), indent=2))
