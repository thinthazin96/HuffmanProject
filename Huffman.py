#Thin Thazin
#CSCI 375
#11/13/2021


a_list = input()

#count frequency of a character
frequencies = {}
for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1

print(frequencies)

#Sort the character in order
for key in sorted(frequencies):
    print(key,frequencies[key])
