import json

data={'spam': (1,2,3), 'eggs': {'a':2, 'b':3}}
serialized = json.dumps(data)
print(data)
print(serialized)
data2 = json.loads(serialized)
print(data2)
print()

with open('data.json', 'wt') as json_file:
    json.dump(data, json_file)

with open('data.json', 'rt') as json_file:
    print(json.load(json_file))