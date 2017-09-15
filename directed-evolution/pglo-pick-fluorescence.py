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
ara_vol=2.5

grow_plate = p.ref("grow_plate", cont_type="96-flat", storage="cold_4")
p.fluorescence(grow_plate, grow_plate.wells_from(0,num_picks*3),
               excitation="483:nanometer", emission="535:nanometer",
               dataref="grow_plate")

print json.dumps(p.as_dict(), indent=2)
