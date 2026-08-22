str =input("enter the string: ")
substr = input("enter the substring: ")
def check_substring(str, substr):
    if substr in str:
        return True
    else:   
        return False

print(check_substring(str, substr))