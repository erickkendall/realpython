import re

def is_digit(string):
    try:
        float(string)
        return True
    except:
        return False


print (is_digit("3"))
print (is_digit("  3  "))
print (is_digit("-3.23"))
print ()
print (print("Fail"))
print (is_digit("3-4"))
print (is_digit("  3   5"))
print (is_digit("3 5"))
print (is_digit("zero"))
print (is_digit("7"))

