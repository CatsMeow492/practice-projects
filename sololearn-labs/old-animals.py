ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]

number = int(input())

old_animals = filter(lambda x: x > number, ages)

old_animals = len(list(old_animals))

print(old_animals)