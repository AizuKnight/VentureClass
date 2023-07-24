# Building another translator using files

import re
input_path = "./FileTranslatorInput.txt"
output_path = "./FileTranslatorOutput.txt"
try:
    input = open(input_path, "r")
    output = open(output_path, "w")
    for line in input:
        output.write(re.sub("[AEIOUaeiou]", "g", line))
except FileNotFoundError as err:
    print(f"Error: {input_path} seems not to exist.")
