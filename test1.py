def run_test():
    print("Test 1 - dictionaries")

me = {
    "first": "Jordi",
    "last": "Bañuelos",
    "age": 22,
    "hobbies": [],
    "address": {
        "street": "Jordi's lair'",
        "number": "22-B",
        "city": "Jorditropolis",
        "state": "Jordiland",
        "zip": "92101"
    }
}

print(me)

print(me["first"])

# print full mame
print(me["first"], me["last"])

# change values
me["age"] = me["age"] + 1
me["age"] = 99

# add new keys
me["preferred color"] = "red"
print(me)

# check if exists
if "middle_name" in me: # Checks for existence
    print(me["middle_name"])

# Print the full address on a single line
address = me["address"]
print("-------- Address --------")
print(address)
print(type(address))

print(f'{address["street"]} #{address["number"]}, {address["city"]}, {address["state"]}, {address["zip"]}')

run_test()