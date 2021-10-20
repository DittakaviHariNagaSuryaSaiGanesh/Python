# if given input is str => false
# if given input is int => true
# if given input is both combo of str and int => false

''' isalnum '''

'''a = str(input())
if(a.isalnum()):
    print("yes")'''

'''num = input()
if(num.isalpha()):
    print("false")
elif(num.isdigit()):
    print("true")
else:
    print("false")'''



#string is given
#in line1 pirnt it it
#in line2 print number of uppercase char
#in line3 print number of lowercase char

'''n = input()
print(n)
l = 0
u = 0
for i in n:
    if(i != ' ' and i.isupper()):
        u+=1
    elif(i != ' ' and i.islower()):
        l+=1
print('Upper case characters: ' + str(u))
print('Lower case characters: ' + str(l))'''


#sorting of n number array

'''num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
arr.sort()
print(arr)'''



#print yes if the second number is last digits of first number
#else no

'''num1 = int(input())
num2 = int(input())
num3 = len(str(num2))
if(num1 % (int(pow(10,num3))) == num2):
   print("yes")
else:
    print("no")'''


#reverse of a number

#method:- 1
'''num = input()
b = reversed(num)
print(list(b))'''

#method:- 2
'''a = input()
b = str(a)
c = b[::-1]
print(c)'''

#method:- 3
'''a = int(input())
s = 0
while(a != 0):
    s = s * 10 + a % 10
    a = a//10
print(s)'''


#Swapping of two numbers
'''a = input('Enter first number: ')
b = input('Enter second number: ')
temp = a
a = b
b = temp
print(a)
print(b)
'''

#Prime Number
'''a = int(input('Enter a number: '))
i = 1
count = 0
while(i <= a):
    if(a%i == 0):
        count = count+1
    i = i + 1
if(count == 2):
    print('Prime number')
else:
    print('composit number')
'''

#Reverse of a number

'''num = int(input('Enter a number: '))
s = 0
while(num > 0):
    s = s*10 + int(num%10)
    num = int(num/10)
print(int(s))
'''

#if Pallindrom or not

'''num1 = int(input('Enter a number: '))
num2 = num1
s = 0
while(num1 > 0):
    s = s * 10 + int(num1 % 10)
    num1 = int(num1 / 10)
if(s == num2):
    print('Given number is pallindrom')
else:
    print('Given number is not pallindrom')
'''

#Factorial of a number

'''num = int(input('Enter a number'))
i = 1
pro = 1
while(i <= num):
    pro = int(pro * i)
    i = i + 1 
print('The factorial of a number: ', pro)
'''

#Fabonacci series

'''num = int(input('Enter a number: '))
i = 1
s = 0
f1 = 1
f2 = 1
print(f1)
print(f2)
while(i <= num):
    s = f1 + f2
    print(s, " ")
    f1 = s
    f2 = i
    i = i + 1
'''

#max and min element in an array without using max() and min() fun

'''arr = []
n = int(input('Enter the size of array:'))

for i in range(n):
    arr.append(input())
max_ele = arr[0]
for i in range(1,n):
    if(max_ele < arr[i]): #if min element condition= min_ele > arr[i]
        max_ele = arr[i]
print(max_ele)'''

#sum of array elements

'''n = int(input('Enter the size of array:'))
arr = []
s = 0

for i in range(n):
    arr.append(int(input()))
for i in range(n):
    s = s + arr[i]
print(s)'''

#swapping the first and last element of the list
'''n = int(input('Enter the size of the array:'))
arr = []

for i in range(n):
    arr.append(int(input()))
temp = arr[0]
arr[0] = arr[n-1]
arr[n-1] = temp
print(arr)'''

#swapping of any two numbers in an array
n = int(input('Enter the size of array: '))
a = int(input('Enter the position of element1: '))
b = int(input('Enter the position of element2: '))
arr = []
fo

