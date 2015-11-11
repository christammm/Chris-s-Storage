__author__ = 'Jabari'

# TUPLES CANNOT BE CHANGED AFTER BEING CREATED

pi_tuple = (3,1, 4, 1, 5, 9)

# Cast list to tuple
new_tuple = list(pi_tuple)

# Cast tuple to list
new_list = tuple(pi_tuple)

print(pi_tuple)
print(new_tuple)
print(new_list)

print("Length = ", len(pi_tuple))
print("Minimum = ", min(pi_tuple))
