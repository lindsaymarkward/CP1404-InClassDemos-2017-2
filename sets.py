# Sets demo code for CP1404, 2017-2

subjects_cp = {'CP1401', 'CP1402', 'CP1404', 'CP1406'}
subjects_maths = {'MA1000', 'MA1003', 'MA1008'}
my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}

# What do these operations mean? (Look it up!)
print(my_subjects - your_subjects)
print(my_subjects | your_subjects)
print(my_subjects & your_subjects)
print(my_subjects ^ your_subjects)

# diff = subjects_cp - my_subjects
# print(diff)
#
# diff = my_subjects - subjects_cp
# print(diff)
#
# diff = subjects_maths - my_subjects
# print(diff)
