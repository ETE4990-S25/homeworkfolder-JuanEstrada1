from functools import reduce

# 1. Basic Lambda Function
is_even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even_or_odd(5))  # Output: Odd
print(is_even_or_odd(8))  # Output: Even

# 2. Advanced Lambda Function (Sum of a List)
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15

# 3. Sorting with Lambda
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people_sorted = sorted(people, key=lambda person: person[1])  # Sorting by age
print(people_sorted)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

# 4. Filtering with Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# 5. Mapping with Lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 6. Reducing with Lambda
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 362880

# 7. Enumerate with Lambda
tasks = ["Task1", "Task2", "Task3"]
enumerated_tasks = list(enumerate(tasks, start=1))
print(enumerated_tasks)  # Output: [(1, 'Task1'), (2, 'Task2'), (3, 'Task3')]

# 8. Zip with Lambda
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 20]
zipped_list = list(zip(names, ages))
print(zipped_list)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 20)]

#Used ChatGPT for help