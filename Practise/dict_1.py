import operator
from collectionsdef import OrderedDict

d = {1: "Prachi", 2: "Nishant", 3: "Kumar", 4: "Sinha"}

sort_str = []
for key, value in d.items():
    print(value)

    sort_str.append(value)

sort_d = sorted(d.items(), key=operator.itemgetter(0))
sort_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
print(sort_d)



t = OrderedDict(sorted(d.items()))
print(t)

print(type(sort_str))
print(sort_str)

print(len(sort_str))
print(sort_str.sort())



desc_str = sort_str.sort(reverse=True)

print(desc_str)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)


