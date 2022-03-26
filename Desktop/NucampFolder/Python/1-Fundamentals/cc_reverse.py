def reverse(str):
    return str[::-1]


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))


def capitalize(str2):
    return str2[0:1].upper() + str2[1:]


name2 = input("Type your name without a capital letter: ")
print("Here it is fixed: ", capitalize(name2))
