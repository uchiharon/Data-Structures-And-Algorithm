'''def reverseWord(words):
    return " ".join(words.split()[::-1])

test = "Good day sunny"

print(reverseWord(test))'''

'''def reverseWord(words):
    temp = words.split()
    i = 0
    j = len(temp) - 1
    while i <= j:
        temp[i], temp[j] = temp[j], temp[i]
        i += 1
        j -= 1
    return " ".join(temp)

test1 = "Time to go home lad"

print(reverseWord(test1))'''


'''def reverseWord(words):
    return words[::-1]

test1 = "Time to go home lad"

print(reverseWord(test1))'''

import string


def reverseword(words):
    temp1 = list(words)
    
    i = 0
    j = len(temp1) - 1

    while i <= j:
        temp1[i], temp1[j] = temp1[j], temp1[i]
        i += 1
        j -= 1

    return "".join(temp1)


test2 = "Let us go home"
print(reverseword(test2))
