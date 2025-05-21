# 1
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])  # Example favorite

# 2
print(x[-2])

# 3
x = list(x)
x[1] = "itel"
x = tuple(x)

# 4
x = list(x)
x.append("Huawei")
x = tuple(x)

# 5
for phone in x:
    print(phone)

# 6
x = list(x)
x.pop(0)
x = tuple(x)

# 7
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu", "Mbale"])

# 8
(city1, city2, city3, city4, city5) = cities

# 9
print(cities[1:4])

# 10
fnames = ("Ali", "Sara")
lnames = ("Khan", "Smith")
combined = fnames + lnames

# 11
colors = ("red", "green", "blue")
print(colors * 3)

# 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))
