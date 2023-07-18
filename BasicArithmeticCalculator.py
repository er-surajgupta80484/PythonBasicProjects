#Basic Arithmetic Calculator which will take two inputs from user and perform the operation chosen by user


#Take two inputs from user
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))

#create a dictionary of the available choices for user
operationDic={1:'Addition',2:'Subtraction',3:'Multiplication',4:'Division',5:'Quotient',6:'Remainder'}

#print the available choices on screen
for items in operationDic:
    print(f"{items} : {operationDic[items]}")

#get user's choice
choice=int(input("What operation you want me to perform : "))

#create a dictionary to perform operation as per choices; keys should be same as availableChoices
resultDic={1:num1+num2,2:num1-num2,3:num1*num2,4:num1/num2,5:num1//num2,6:num1%num2}
#perform operation based on the choice; alse check if the choice is valid
if(choice>0 and choice<=len(operationDic)):
    print(f"{operationDic[choice]} of {num1} and {num2} is {resultDic[choice]}")
else:
    print(f"Kindly choose values between 1 to {len(operationDic)}")


