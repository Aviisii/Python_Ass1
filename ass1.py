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

#5
f = int(input("Enter a Number: "))
g = int(input("Enter next Number: "))
f, g = g, f
print("After Swapping\n" "First variable is: ",f ,"\nSecond variable is: ",g)



#Chapter 2
#1
h = int(input("Enter a number: "))
remain = h % 2
if remain >0:
    print("This is an odd number.")
else:
    print("This is an even number.")

#2
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter next integer: "))
if num1 > num2:
    print(num1, "is the largest.")
else:
    print(num2, "is the largest.")

#3
i_1 = int(input("Enter an integer: "))
i_2 = int(input("Enter next integer: "))
i_3 = int(input("Enter last integer: "))
print("The largest number: ",max(i_1, i_2, i_3))

#4
i = int(input("Enter a year: "))
j = i%4
k = i%100
l = i%400
if j==0:
    if k==0:
        if l==0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
'''

#5
m = int(input("Enter your marks: "))
if m >= 60:
    if m >= 70:
        if m >= 80:
            if m >= 90:
                print("Grade A")
            else:
                print("Grade B")
        else:
            print("Grade C")
    else:
        print("Grade D")
else:
    print("Grade F")
