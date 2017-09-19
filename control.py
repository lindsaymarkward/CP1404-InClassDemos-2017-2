# print("Hello world")
# age = int(input("Age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Child")

total = 0
number_of_people = 0

age = int(input("Age: "))
while age >= 0:
    total += age
    number_of_people += 1
    age = int(input("Age: "))

if number_of_people == 0:
    print("No people.\n\tThis is more meaningful.\n Sorry about the '?'.")
else:
    average = total / number_of_people
    print(average)
