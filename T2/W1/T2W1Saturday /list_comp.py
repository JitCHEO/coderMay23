
# newlist = [expression for item in iterable if condition == True]

squares = []
for num in range(1,10):
    squares.append(num ** 2)

print(squares)

list_squares = [ num ** 2 for num in range(1,10)]

print(list_squares)


# EXAMPLE2

squares = []
for num in range(1,10):
    if num % 2 == 0:
        squares.append(num ** 2)

print(squares)

list_squares = [ num ** 2 for num in range(1,10) if num % 2 == 0]

print(list_squares)

# EXAMPLE3
items = [
            {
                "fruit": "mango",
                "number": 2
            },
            {
                "fruit": "apple",
                "number": 3
            },
            {
                "fruit": "kiwi",
                "number": 1
            }
        ]

new_items = [ fruit for fruit in items if fruit["number"] >= 2 ]
print(new_items)
