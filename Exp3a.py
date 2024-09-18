# def reverse_string_for_loop(s):
#     reversed_string = ""
#     for char in s:
#         reversed_string = char + reversed_string 
#     return reversed_string


# s = "hello"
# print(reverse_string_for_loop(s)) 

def reverse_string_while_loop(s):
    reversed_string = ""
    index = len(s) - 1  
    while index >= 0:
        reversed_string += s[index]  
        index -= 1  
    return reversed_string


s = "hello"
print(reverse_string_while_loop(s))  
