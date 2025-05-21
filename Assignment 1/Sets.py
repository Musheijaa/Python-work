# 1
beverages = set(["tea", "coffee", "juice"])

# 2
beverages.update(["milk", "soda"])

# 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

# 4
mySet.discard("kettle")

# 5
for item in mySet:
    print(item)

# 6
myset = {"pen", "book", "paper", "ink"}
mylist = ["ruler", "eraser"]
myset.update(mylist)

# 7
ages = {20, 25}
names = {"Tom", "Jerry"}
combined = ages.union(names)
