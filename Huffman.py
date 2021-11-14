#Thin Thazin
#CSCI 375
#11/13/2021


a_list = input()

frequencies = {}
for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1

print(frequencies)

for key in sorted(frequencies):
    print(key,frequencies[key])
