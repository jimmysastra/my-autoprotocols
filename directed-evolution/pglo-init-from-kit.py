import json
from autoprotocol.protocol import Protocol
from autoprotocol.container import WellGroup

# perform pGLO Bacterial Transformation Kit experiment made by BIO-RAD.

p = Protocol()

test_plates = [];
transform_sln = p.ref("transform_sln", id="ct1ajdhxkq53gx", cont_type="micro-2.0", storage="cold_4")
pglo = p.ref("pglo", id="ct1ajdhxkrfv86", cont_type = "micro-2.0", storage="cold_4")
culture = p.ref("culture", id="ct1ajdhza2rxk3", cont_type="6-flat", storage="cold_4")
ecoli_source = p.ref("ecoli_src", id="ct1ajdhz9zmrf2", cont_type="6-flat", storage="cold_4")
transformation_plate = p.ref("transformation_plate", cont_type="96-pcr", discard=True)
lb_media = "rs17bafcbmyrmh"
growth_plate = p.ref("growth_plate", cont_type="96-deep", storage="cold_4")
#culture plate layout:
#0:lb 1:amp 2:amp/ara 
#3:lb 4:amp 5:amp/ara

#0:no_pglo 1:pglo 2:pglo
#3:no_pglo 4:no_pglo 5:pglo


p.transfer(transform_sln.well(0), transformation_plate.wells_from(0,2), "150:ul")
p.incubate(transformation_plate, "cold_4", "5:minute")
p.autopick(ecoli_source.all_wells(), transformation_plate.wells_from(0,2))
p.transfer(pglo.well(0), transformation_plate.well(0), "10:ul")

for w in transformation_plate.wells_from(0,2):
  p.mix(w,volume="75:microliter")

sources = WellGroup([transformation_plate.well(0)] * 2 + [transformation_plate.well(1)] * 2)
dests = WellGroup(
  transformation_plate.wells_from(12,2,columnwise=True) + 
  transformation_plate.wells_from(13,2,columnwise=True))
p.transfer(sources, dests, "50:ul")
p.thermocycle(transformation_plate, 
  [
    {"cycles": 1,
      "steps": [
        {"temperature": "4:celsius",
        "duration": "10:minute"},
        {"temperature": "42:celsius",
        "duration": "50:second"},
        {"temperature": "4:celsius",
        "duration": "2:minute"}
      ]
     }
   ],
   volume="50:microliter"
   )


p.provision(lb_media, growth_plate.wells_from(0,2), "350:ul")

for row in range(3):
  p.stamp(transformation_plate.well(row * 12), growth_plate.well(0),
          "50:ul", shape={"rows":1, "columns":12}, mix_after=True)


p.incubate(growth_plate, "ambient", "10:minute")

p_glo_wells = culture.wells([1,2,5])
no_p_glo_wells = culture.wells([0,3,4])
for w in p_glo_wells:
  p.spread(growth_plate.well(0), w, "50:ul")
for w in no_p_glo_wells:
  p.spread(growth_plate.well(1), w, "50:ul")

p.incubate(culture, "warm_37", "24:hour")
p.image_plate(culture, mode="top", dataref="pglo_plate1")

print json.dumps(p.as_dict(), indent=2)
