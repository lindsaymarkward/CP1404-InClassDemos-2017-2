names_to_ages = {"Bill": 21, "Jane": 34, "Sven": 56}


# d = {name: age for name, age in names_to_ages.items() if name[0] == "S"}
#
# print(d)
# # for name in names_to_ages:
# #     names_to_ages[name] += 1
# #     print(name, names_to_ages[name])
# #
# #
# # for name, age in names_to_ages.items():
# #     print(name, age)
#
#
# # words = ["a", "b", "a"]
# # word_to_count = {}
# # for word in words:
# #     if word in word_to_count:
# #         word_to_count[word] += 1
# #     else:
# #         word_to_count[word] = 1
# #
# #
# # word_to_count = {}
# # for word in words:
# #     try:
# #         word_to_count[word] += 1
# #     except KeyError:
# #         word_to_count[word] = 1

def find_older(people, threshold_age):
    old_people = []
    for name, age in people.items():
        if age >= threshold_age:
            old_people.append(name)
    # return old_people
    return [name for name, age in people.items() if age >= threshold_age]

# print(find_older(names_to_ages, 50))

class LindsayList(list):
    def whatever(self):
        print("whatever")

my_list = list()
print(my_list)
my_list.append('a')

my_lindsay_list = LindsayList()
print(my_lindsay_list)
my_lindsay_list.append('b')
my_lindsay_list.whatever()

