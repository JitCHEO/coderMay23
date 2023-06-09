# given a string find out if the string is palindrome or not
# nitin <-> nitin

# define a function that finds out whether the string is palindrome or not
def is_palindrome(str):
    
    # reverse the string
    reverse = str[::-1]
    
    # compare the strings
    # return outcome
    return reverse == str

    # option2 (but longer lines)
    # if reverse == str:
    #     return True
    # else:
    #    return False


# input from the user
word = input("Enter your word> ")

# check user is palidrome or not
palindrome_check = is_palindrome(word)

# display output
# if/else to print palindrome

if palindrome_check:
    print(f"{word} is a palindrome string")
else:
    print(f"{word} is not a palindrome string")

