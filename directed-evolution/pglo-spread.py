import json
from autoprotocol.protocol import Protocol
from autoprotocol.container import WellGroup
from autoprotocol_utilities.resource_helpers import ref_kit_container
p = Protocol()

"""
after growing up in a flask, put the glowing bacteria in a tube and run the below protocol to do a serial dilution, 
then spread 
"""
num_dilutions = 4 #dilute 1:100 each time

pglo_bact = p.ref("pglo_bact", id="ct1am4uegqerfk", cont_type="micro-2.0", storage="cold_4")
serial_dilution = p.ref("serial_dilution", cont_type="96-pcr", storage="ambient")
p.provision("rs17bafcbmyrmh", serial_dilution.wells_from(0, 4), "148.5:microliter")
agar = p.ref("agar", cont_type="6-flat", storage="cold_4")
#agar = ref_kit_container(p, "agar", container="6-flat", kit_id="kit17sbb845k7c3", store="cold_4")



p.transfer(source=pglo_bact.well(0), dest=serial_dilution.well(0), volume="1.5:microliter", mix_after=True, mix_vol="100:microliter") #1:100 dilution
for w in range(num_dilutions-1): #1E-4, 1E-6, 1E-8 dilutions
  p.transfer(source=serial_dilution.well(w), dest=serial_dilution.well(w+1), volume="1.5:microliter", one_tip=True, mix_after=True,mix_vol="100:microliter")

for w in range(3):
  p.spread(serial_dilution.well(w+1), agar.well(w), "50:ul")

#num_images=4
#for i in range(num_images):
#  p.image_plate(agar, mode="top", dataref="agar"+str(i))
#  p.incubate(agar, "warm_37", str(24/num_images)+":hour")

p.incubate(agar, "warm_37", "24:hour")

print json.dumps(p.as_dict(), indent=2)
