# Python program to implement
# ROT13 Caesar cipher

# ********************************************************************* #

# This Function decrypt each letter in the string
# according to the shift 13
def decipher(letter_case, i):
    shift = 13
    i_index = letter_case.index(i)
    i_shift = i_index + shift
    if i_shift >= len(letter_case):
        i_shift -= len(letter_case)
    ans = letter_case[i_shift]
    return ans

# The main function check for lower and upper case letters
# as well as special characters.
# The function decipher is called in this function


def rot13(message):
    result = ''
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    for i in message:
        if i in upper_case:
            new_letter = decipher(upper_case, i)
            result = result + new_letter
        elif i in lower_case:
            new_letter = decipher(lower_case, i)
            result = result + new_letter
        else:
            result = result + i
    return result


#********EXAMPLES*************#

print(rot13('TRRXF SBE TRRXF'))
print(rot13('@[`{'))
print('GEEKS FOR GEEKS')
print(rot13("EBG13 rknzcyr."))
print(rot13("How can you tell an extrovert from an\nintrovert"))

