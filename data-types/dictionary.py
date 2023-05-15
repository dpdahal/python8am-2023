# what is dictionary?
# dictionary is a collection of key-value pairs
# dictionary is mutable
# dictionary is unordered

# how to create dictionary?

data = {
    "name": "sagar",
    "age": 22,
    "address": {
        "city": "kathmandu",
        "country": [
            "nepal",
            "india"
        ]
    }
}

print(f"my name is {data['name']}")
print(f"I live in {data['address']['city']}")
print(f"I live in {data['address']['country'][0]}")

#
# print(data['name'])

# data1 = ['sagar', 20, 'kathmandu']
# print(data1[0])


# data = [
#     ['sagar', 20, 'kathmandu'],
#     ['ram', 20, 'kathmandu'],
# ]
#
# print(data[1][0])
