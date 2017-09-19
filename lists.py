"""Lists demo code, in-class, CP1404 2017-2."""

numbers = [9, 23, -3, 12, 0, 0, -1]

things = list("Things")


# print(things)
# things = [1, 'a', True]
# print(things)

# numbers = []
# for n in range(1, 10):
#     if n % 2 == 0:
#         numbers.append(n)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(calculate_average([]))
