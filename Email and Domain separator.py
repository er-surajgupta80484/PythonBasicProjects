#Program to separate domain and user id from the given email id

email=input("Enter email: ")
values=email.split(sep='@')
print(f"User ID is {values[0]} and Domain is {values[1]}")