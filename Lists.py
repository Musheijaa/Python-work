# 1
names = ["Alice", "Bob", "Carol", "David", "Eve"]
print(names[1])

# 2
names[0] = "Zara"

# 3
names.append("Frank")

# 4
names.insert(2, "Bathel")

# 5
del names[3]

# 6
print(names[-1])

# 7
new_list = ["A", "B", "C", "D", "E", "F", "G"]
print(new_list[2:5])

# 8
countries = ["Uganda", "Kenya", "Tanzania"]
countries_copy = countries.copy()

# 9
for country in countries:
    print(country)

# 10
animals = ["cat", "dog", "elephant", "giraffe", "ant"]
print(sorted(animals))        # Ascending
print(sorted(animals, reverse=True))  # Descending

# 11
for animal in animals:
    if 'a' in animal:
        print(animal)

# 12
first_names = ["John", "Jane"]
second_names = ["Doe", "Smith"]
full_names = first_names + second_names
