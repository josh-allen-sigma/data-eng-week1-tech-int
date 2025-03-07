# Notes
# Identify if a string is a palindrome (reads the same backwards as forwards) or not.
# For example, "aha" is a palindrome but "camel" is not. Reversing the string is not permitted.
# Is the first half the same as the second half

# ---------------------------------

#  Task 1

def palindrome_identifier(input: str) -> bool:
    for i in range(int(len(input)/2)):
        print(i)
        print(input[i],  input[-i - 1])
        if input[i] != input[-i - 1]:
            print(False)
            return False
    print(True)
    return True


palindrome_identifier('abage')
