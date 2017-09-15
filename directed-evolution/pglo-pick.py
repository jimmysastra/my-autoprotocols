import json
from autoprotocol.protocol import Protocol
from autoprotocol.container import WellGroup
from autoprotocol_utilities.resource_helpers import ref_kit_container

p = Protocol()

#wells 1-4: pglo + bacteria + ara + lb amp
#well 5-8: same but no ara (control)
#well 9-12: no bactera, no ara (control)

num_picks = 4
selected_well=2
grow_vol = 250 #ul
ara_vol=round(grow_vol/32)


grow_plate = p.ref("grow_plate", cont_type="96-flat", storage="cold_4")
agar = p.ref("ct1amxs8eggsk7",  cont_type="6-flat", storage="cold_4")
p.provision("rs18s8x4qbsvjz", grow_plate.wells_from(0, num_picks*3), str(grow_vol)+":microliter") #lb liquid with amp. +2 for controls
arabinose = p.ref("arabinose", cont_type="micro-1.5", storage="ambient")
p.provision("rs185rp3d22ca5", arabinose.wells(0), str(ara_vol*(num_picks) + 25) + ": microliter")  #10% L(+)-Arabinose 

#p.image_plate(agar, mode="top", dataref="agar_plate")
p.autopick(agar.well(selected_well), grow_plate.wells_from(0,num_picks*2))
p.transfer(arabinose.wells(0), grow_plate.wells_from(0,num_picks), str(ara_vol)+":microliter")
p.incubate(grow_plate, "warm_37", "24:hour" , shaking=True)
# platereader settings based on http://ww3.tecan.com/platform/apps/virtualdirectories/gcm/downloads/AN_INF200PRO_enhanced_FI_Bottom_V1_0.pdf
p.fluorescence(grow_plate, grow_plate.wells_from(0,num_picks*3),
               excitation="483:nanometer", emission="535:nanometer",
               dataref="grow_plate")

print json.dumps(p.as_dict(), indent=2)
