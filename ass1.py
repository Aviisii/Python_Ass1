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

#Chapter 3
#1
n = int(input("Enter a number: "))
for i in range (1, 13):
    print(n,"x",i,"=",n*i)

#2
p = int(input("Enter a number: "))
q = 1
if p < 0:
    print("Factroial does not exit")
elif p ==0:
    print("The factorial of 0 is 1")
else:
    for r in range(1,p+1):
        q = q * r
        print ("The factorial of",p,"is",q)

#3
s = int(input("Enter digits: "))
t = 0
while s > 0:
    v = s%10
    t = t+v
    s = int(s/10)
    print("Sum of all digits: ", t)
#crd google

#4
w = input("Enter any number: ")
x = w[::-1]
if x == w:
    print("It is palindromic")
else:
    print("It is not a palindromic")

#5
y = int(input("Enter a number: "))
z = int(input("Enter next number: "))
def hcf(y, z):
    while(z):
        y, z = z, y%z
    return y
print("The HCF or GCD of your number: ",hcf(y,z))


#Chapter 4
#1
aa = "aeiou"
ab = input("Enter your sentence: ")
ab = ab.casefold()
ac = {}.fromkeys(aa,0)
for ad in ab:
    if ad in ac:
        ac[ad] += 1
print(ac)
#crd google

#2

#3
str1 = input("Enter a word: ")
str2 = str1[::-1]
print(str2)

#4
'''
#5
str3 = input("Enter digits from 0 to 9: ")
num = list(map(int, str(str3)))
print("The list of your digits is: ", num)
num.sort()
print("Largest number in the list: ",num[-1])