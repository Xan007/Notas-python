from collections import Counter

inventory = Counter(dogs=23, cats=14, pythons=7)

adopted = Counter(dogs=2, cats=5, pythons=1)
inventory.subtract(adopted)
print(inventory, "Substract")


new_pets = {"dogs": 4, "cats": 1}
inventory.update(new_pets)
print(inventory, "update")


inventory = inventory - Counter(dogs=2, cats=3, pythons=1)
print(inventory, "substract con -")


new_pets = {"dogs": 4, "pythons": 2}
inventory += new_pets
print(inventory, "update con +=")


from collections import Counter
sales = Counter(banana=15, tomato=4, apple=39, orange=30)

# The most common object
sales.most_common(1)


# The two most common objects
sales.most_common(2)


# All objects sorted by count
sales.most_common()


sales.most_common(None)


sales.most_common(20)


##MODA

from collections import Counter

def mode(data):
    counter = Counter(data)
    _, top_count = counter.most_common(1)[0]
    return [point for point, count in counter.items() if count == top_count]