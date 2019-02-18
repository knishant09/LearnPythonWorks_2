set_1 = set(["red", "Blue", "Green"])

print(set_1)

set_1.add("Black")

print(set_1)

set_1.remove("Blue")

print(set_1)

set_1.discard("Yellow")

print(set_1)


set_2 = set(["Purple", "Green", "Red", "Yellow", "Blue"])

print(set_2)

set_union = set_1 & set_2

print(set_union)

set_inter = set_1 | set_2

print(set_inter)



