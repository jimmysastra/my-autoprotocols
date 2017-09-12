from autoprotocol.protocol import Protocol
import json

p = Protocol()
src_plate= p.ref("src_plate", None, "96-pcr", discard=True)
dest_plate= p.ref("dest_plate", None, "384-flat", discard=True)

xfer_vol = [10]*96;
shape_format='SBS96';

# common parameters for all stamps performed
stamp_kwargs = {
  'new_defaults': True,
  'pre_buffer': '10:microliter',
  'blowout_buffer': True,
  'mix_after': True,
  'mix_vol': '30:microliter',
  'repetitions': 5,
  'flowrate': '100:microliter/second',
  'shape_format': shape_format
}

#p.seal(src_plate)
#p.unseal(src_plate)

p.transfer(src_plate.wells_from(0,4), dest_plate.wells_from(0,4),
    ["10:microliter", "20:microliter", "30:microliter", "40:microliter"])

#p.stamp(src_plate, dest_plate, "10:microliter")
#p.cover(dest_plate);
#p.incubate(dest_plate, "warm_37", "30:minute", shaking=False)

#p.stamp(src_plate, dest_plate, xfer_vol, **stamp_kwargs)

print (json.dumps(p.as_dict(), indent=2))
