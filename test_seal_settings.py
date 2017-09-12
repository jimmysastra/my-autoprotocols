from autoprotocol.protocol import Protocol
import json

p = Protocol()
test_plate= p.ref("test_plate", None, "96-pcr", storage="ambient")

def x_seal(protocol, temperature, duration):
    protocol.instructions[-1].data["x_temperature"] = temperature
    protocol.instructions[-1].data["x_duration"] = duration

p.dispense(test_plate,
           "water",
           [{"column": 0, "volume": "10:microliter"},
            {"column": 1, "volume": "20:microliter"},
            {"column": 2, "volume": "30:microliter"},
            {"column": 3, "volume": "40:microliter"},
            {"column": 4, "volume": "50:microliter"},
            {"column": 5, "volume": "60:microliter"},
            {"column": 6, "volume": "70:microliter"},
            {"column": 7, "volume": "80:microliter"},
            {"column": 8, "volume": "90:microliter"},
            {"column": 9, "volume": "100:microliter"},
            {"column": 10, "volume": "110:microliter"},
            {"column": 11, "volume": "120:microliter"}
           ])

p.seal(test_plate)

p.thermocycle(test_plate,
            [
             {"cycles": 1,
              "steps": [{
                 "temperature": "95:celsius",
                 "duration": "30:minute",
                 }]
              }
            ])

p.unseal(test_plate)
p.image_plate(test_plate, mode="top", dataref="test_plate_result")
p.absorbance(test_plate, sample_plate.wells_from(0,12),
             "600:nanometer", "test_reading", flashes=50)

#p.unseal(test_plate)
print (json.dumps(p.as_dict(), indent=2))


