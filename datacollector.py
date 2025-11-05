print("Welcome to the Interactive Personal Data Collector !")

print()

name=str(input(" plsese enter your name :"))
age=int(input(" plsese enter your age :"))
height=float(input(" plsese enter your height in meters :"))
number=int(input(" plsese enter your favoururite number :"))

print()

print("Thank you ! Here is the information we collected:")

print()

print("name:",name,("Type:",type (name),'Memorey address:',id(name),))
print("age:",age,("Type:",type (age),'Memorey address:',id(age),))
print("height:",height,("Type:",type (name),'Memorey address:',id(height),))
print("name:",number,("Type:",type (number),'Memorey address:',id(number),))

print()

a=(2025 - age)

print('Your birth year is approximately :',(a),('based on your age of',age))

print()

print('Thank you for using the personal Data Collector. Goodbye!')

