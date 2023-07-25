#Program to check if password is valid

caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
specials='@_#$!'
char_upper=0
char_lower=0
char_digit=0
char_special=0

print('''Password Rules: \n
      1. Minimum 8 character long
      2. Should have atleast one digit, one upper case letter and one lower case letter
      3. Must contain one special character. Allowed characters are @#_$!
      ''')

input_password=input("Enter a password : ")

if (len(input_password)>=8):
    for char in input_password:
        if char in caps:
            char_upper+=1
        if char in lowers:
            char_lower += 1

        if char in digits:
            char_digit += 1

        if char in specials:
            char_special += 1


    if(char_digit>=1 and char_special>=1 and char_lower>=1 and char_upper>=1):
        print(f"{input_password} is a valid password")
    else:

        print(f"Invalid Password! you password is not following the rules stated above\nConsider including below:")
    if char_upper<1:
        print("Atleast 1 Upper case character")
    if char_lower<1:
        print("Atleast 1 lower case character")
    if char_digit<1:
        print("Atleast 1 digit character")
    if char_special<1:
        print("Atleast 1 special case character")

else:
    print(f"You have entered {len(input_password)} characters. Please enter atleast 8 characters")