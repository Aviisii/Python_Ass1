#Chapter1
#1
'''
a = input("Enter Your Name: ")
print("Hello",a)

#2
b = int(input("Enter a number: "))
c = int(input("Enter Next number: "))
print("The total of your numbers: ", b + c)

#3
d = eval(input("Enter a temperature in Celsius: "))
print("The temperature in Fahrenheit: ",9/5 * d + 32)

#4
e = int(input("Enter seconds: "))
hour = e//3600
hr = e%3600
minute = hr//60
second = hr%60
print(" Hour: ",hour ,"\n Minute: ",minute, "\n Second: ",second)

'''
#5
f = int(input("Enter a Number: "))
g = int(input("Enter next Number: "))
f, g = g, f
print("After Swapping\n" "First variable is: ",f ,"\nSecond variable is: ",g)