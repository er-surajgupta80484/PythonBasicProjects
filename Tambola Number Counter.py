#program to get a number to play tambola game between 0-90 and called number cant be repeated again

import random
numlist=[]
viewls=[]
print("Welcome to Tambola! Press enter to start the game and type quit & hit enter to quit\nAt any point during game, if you want to view the numbers, Then TYPE view\n")
choice=input("Press enter to start the game")
loop_input=''
loop_counter=0
if choice=='':
    while loop_input!='quit':
        num=random.randint(1,90)
        if num in numlist:
            continue
        else:
            loop_input = input("Press enter to generate new number")
            if loop_input == '':
                print(num)
                numlist.append(num)
                viewls.append(num)
                loop_counter+=1
            if str.lower(loop_input)=='view':

                viewls.sort()
                print(viewls)

            if str.lower(loop_input)=='quit' or loop_counter==90:
                break
print(f"Game Over! All 90 numbers as they called out\n\nnumbers called are {numlist}")

#below is the sample code to test if numbers are all unique by converting list to set and match the count of elements in set and list. because set contains unique values only.
#count=0
#myset=set()
#for element in numlist:
#    count+=1
 #   myset.add(element)
#print(count)
#count=0
#for element in myset:
 #   count+=1
#print(count)

