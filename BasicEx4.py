# Building a translator

def translate(input):
    for i in list(input):
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or \
                i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            print("g", end="")
        else:
            print(i, end="")


translate(input("Type a sentence: "))
