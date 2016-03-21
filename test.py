

def is_palindrome(str):
    str = list(str.lower())
    array = []
    for ch in str:
        if (ch.isalnum() == True):
            array.append(ch)
    string = ''.join(array)
    array.reverse()
    return (string == ''.join(array))

print(is_palindrome('Emma'))
print(is_palindrome('emme'))
print(is_palindrome('em m e'))
print(is_palindrome('Rac eca r'))
