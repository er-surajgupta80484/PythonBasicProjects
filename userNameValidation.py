'''
User Name must satisfy below condition:
1. Should not be starting with a digit
2. Should be alphanumeric
3. minimum 6 characters long
4. Special characters are optional but only one character allowed either .(dot) or _(UnderScore)
'''
print(__doc__)
username=input("Enter Username: ")
alphacount=0
numcount=0
spcount=0
allowedSpecial='_.'
unallowed=0
if(len(username)>=6):
    if(username[0].isdigit()==False):
        for i in username:

            if(i.isdigit()==True):
                numcount+=1
            if i.isalpha()==True:
                alphacount+=1
            if(i in allowedSpecial):
                spcount+=1
            else:
                unallowed=1
        if unallowed==0:

            if (spcount <= 1):
                if(numcount>=1 and alphacount>=1):

                    print("Congratulations! User Name is valid")
                else:
                    print("Either Alphabet or digit is missing")
            else:
                print("Please enter only one character. Check rule no. 4")
        else:
            print("Special character allowed is dot and underscore only. Please check rule no. 4")
    else:
        print("Username can not be started with a digit. Please enter an alphabet")
else:
    print("Please Enter more than 6 characters")
