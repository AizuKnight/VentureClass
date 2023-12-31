# Implemented a speed meter
# Assumed that data was taken every second

# Describe how to retrieve data later

import math
import time


numbers = [
    [
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■"
    ], [
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■"
    ], [
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "■■■■■■■■■■■■■",
        "■■           ",
        "■■           ",
        "■■           ",
        "■■■■■■■■■■■■■"
    ], [
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "■■■■■■■■■■■■■"
    ], [
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■"
    ], [
        "■■■■■■■■■■■■■",
        "■■           ",
        "■■           ",
        "■■           ",
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "■■■■■■■■■■■■■"
    ], [
        "■■■■■■■■■■■■■",
        "■■           ",
        "■■           ",
        "■■           ",
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■"
    ], [
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "           ■■"
    ], [
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■"
    ], [
        "■■■■■■■■■■■■■",
        "■■         ■■",
        "■■         ■■",
        "■■         ■■",
        "■■■■■■■■■■■■■",
        "           ■■",
        "           ■■",
        "           ■■",
        "■■■■■■■■■■■■■"
    ]
]


def read_file(f_name):
    with open(f_name, mode="r") as f:
        position = [list(map(lambda x: round(float(x), 2), line.split(",")[4:7]))for line in f.readlines()[1:]]
    return position


def print_7seg(num):
    if num >= 1000:
        return
    elif num >= 100:
        digit = 3
        hundred = int(num / 100)
        ten = int(int(num % 100) / 10)
        one = int(int(num % 100) % 10)
        for line in range(9):
            print(numbers[hundred][line] + "    " + numbers[ten][line] + "    " + numbers[one][line])
    elif num >= 10:
        digit = 2
        ten = int(num / 10)
        one = int(num % 10)
        for line in range(9):
            print(numbers[ten][line] + "    " + numbers[one][line])
    else:
        digit = 1
        for line in range(9):
            print(numbers[num][line])
    print("                 " * digit + "cm/s")


number = int(input("Which sample do you use? (1-9): "))
file_name = "sample_" + str(number) + ".csv"
position_list = read_file(file_name)

for i in range(len(position_list)-1):
    unit = 1
    velocity = math.dist(position_list[i], position_list[i+1]) / unit
    print_7seg(round(velocity))
    time.sleep(unit)
