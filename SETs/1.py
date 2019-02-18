import os

x = set()
print(x)
#Create a non empty set
n = set([0, 1, 2, 3, 4])
print(n)


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

for d in Days:
    print(d)

Days.add("Sunday")
print(Days)

Days.discard("Sunday")
print(Days)

Day1 = set(["Mon", "Tues", "Wed"])
Day2 = set(["Fri"])

AllDays = Day1| Day2
print(AllDays)




