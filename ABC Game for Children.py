#ABC Game for toddlers

#creating a dictionary of alphabets
alphaDic={'a':'Apple',
'b':'Ball',
'c':'Cat',
'd':'Dog',
'e':'Elephant',
'f':'Fox',
'g':'Gun',
'h':'Hut',
'i':'Ink',
'j':'Jug',
'k':'Kiwi',
'l':'Litchi',
'm':'Mango',
'n':'Number',
'o':'Oscar',
'p':'Parrot',
'q':'Queen',
'r':'Rat',
's':'Star',
't':'Turtle',
'u':'Umbrella',
'v':'Van',
'w':'Walk',
'x':'Xerox',
'y':'Yogurt',
'z':'Zebra'}

print("Welcome to ABC Game. \n"
    "Type quit to quit the game")
alphabet=""
while(alphabet!='quit'):   #keep running the game until user types quit
    alphabet = input("") #cursor asks for input without displaying message
    alphabet = alphabet.lower() #convert into lower string as our keys are in lower case in dictionary but user can input uppercase too
    if(len(alphabet)==1):  #set the limit of character input to 1 character only
        if alphabet >= 'a' and alphabet <= 'z': #check if entered character is alphabet only.
            print(f"{alphabet.upper()} for {alphaDic[alphabet]}")
        else:
            print("Enter only alphabet (a-z) or (A-Z)") #if character input is non alphabet then display this message
    else:
        print("Enter only one character") # if user inputs more than one character, then input this message


