
in_file = open("data.txt")
# text = in_file.read()
# print(repr(text))
# print(text.split())
# print(in_file.readline())
# input()
# print(in_file.readline())

for line in in_file:
    # print(line)
    parts = line.split(',')
    # print(parts)
    name = parts[0]
    age = int(parts[1])
    print(name, age)

in_file.close()
