
tempDict={1:'Celsius',2:'Fahrenheit', 3:'Kelvin'}
def display_units():

    for i in range(1,4):
        print(f"{i}. {tempDict[i]}")
    userinput=int(input("Enter your choice : "))
    return userinput
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 1:
        if output_scale == 2:
            return value * 1.8 + 32
        elif output_scale == 3:
            return value + 273.15
        else:
            return value
    elif input_scale == 2:
        if output_scale == 1:
            return (value - 32) / 1.8
        elif output_scale == 3:
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 3:
        if output_scale == 1:
            return value - 273.15
        elif output_scale == 2:
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value
#main program starts here
print("Temperature unit you want to convert from : ")
convert_from=display_units()
print("Temperature unit you want to convert into : ")
convert_to=display_units()
temp=float(input(f"Enter Temperature in {tempDict[convert_from]}: "))
result = convert_temperature(temp, convert_from, convert_to)
print(f"{temp} degree {tempDict[convert_from]} to {tempDict[convert_to]} is {result} degree {tempDict[convert_to]}")