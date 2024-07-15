import random

def mix(str1, str2):
    final_str = "".join(random.sample(str1 + str2, len(str1) + len(str2)))
    return final_str