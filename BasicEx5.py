# Building a translator with re

import re
print(re.sub("[AEIOUaeiou]", "g", input("Type a sentence: ")))
