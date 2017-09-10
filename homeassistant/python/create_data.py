import random

items = range(10)

results = []

while len(results) < 1:
    number = random.sample(items, 1)
    if number not in results:
        results.append(number)

print resultsi(0)


