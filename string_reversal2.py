def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
str = "reversal"
print(str[1:])
print(str[0])
print(str[::-1])
reverse = string_reverse(str)
print(reverse)