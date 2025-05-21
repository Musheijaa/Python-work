# 1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

# 2
Shoes["brand"] = "Adidas"

# 3
Shoes["type"] = "sneakers"

# 4
print(Shoes.keys())

# 5
print(Shoes.values())

# 6
print("size" in Shoes)

# 7
for key, value in Shoes.items():
    print(key, value)

# 8
Shoes.pop("color")

# 9
Shoes.clear()

# 10
mydict = {"fruit": "mango", "color": "yellow"}
copydict = mydict.copy()

# 11
nested = {
    "child1": {"name": "Ann", "age": 5},
    "child2": {"name": "Tom", "age": 7}
}
