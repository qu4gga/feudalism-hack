from pyamf import sol
import json
#import pprint


data = sol.load("saves/original/Feudalism_Save_1.sol")

print(data["MAIN_HERO"]["STR"])

for key, value in data.items():
    if isinstance(value, dict) and "STR" in value:
        print(key, value["STR"])

#default
#for key, value in data.items():
#    print(f"{key:20} {type(value).__name__:8} {value!r}")

#json
# default=str converts non-JSON types (like dates or custom AMF objects) into readable strings
#formatted_output = json.dumps(data, indent=4, default=str, sort_keys=True)
#print(formatted_output)

#pprint
#pp = pprint.PrettyPrinter(indent=2, width=80, depth=4)
#pp.pprint(data)



