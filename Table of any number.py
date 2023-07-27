#Program to find the table of any number upto n

num=int(input("Enter the number : "))
n=int(input("Table upto : "))
for i in range(1,n+1):
    print(f"{num} * {i} = {num*i}")

