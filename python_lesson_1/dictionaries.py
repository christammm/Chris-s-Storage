__author__ = 'Jabari'

# Made of values with Unique keys for each values (MAPS)
# Structure key:value

siblings = {"oldest":"Jalia", "middle":"Jabari", "youngest":"Jelani"}


print(siblings)

# Find value
print("oldest = ", siblings["oldest"])

# Delete k:v pair
del siblings["oldest"]

print(siblings)

print("oldest = ",siblings.get("oldest"))

print(siblings.keys())
print(siblings.values())



