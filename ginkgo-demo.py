from autoprotocol.protocol import Protocol
import json

p = Protocol()
ginkgo_plate = p.ref("ginkgo_plate", None, "384-flat", storage="ambient")
tx_plate = p.ref("tx_plate", None, "384-flat", storage="ambient")

p.absorbance(ginkgo_plate, ginkgo_plate.all_wells(),
             "475:nanometer", "tx_absorbance", flashes=1)
p.image_plate(tx_plate, mode="top", dataref="tx_image_ng")
p.transfer(source=tx_plate.well("E19"),
           dest=tx_plate.well("K12"),
           volume="80:microliter")
p.image_plate(tx_plate, mode="top", dataref="tx_image_good")

p.absorbance(tx_plate, tx_plate.all_wells(),
             "475:nanometer", "ginkgo_absorbance", flashes=1)

print (json.dumps(p.as_dict(), indent=2))
