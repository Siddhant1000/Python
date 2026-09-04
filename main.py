# a = str(input("Enter your gender"))

# if a == "male" or a == "Male":
#     print("Good Morning Sir")
# else:
#     print("Good Morning Maam")

# a = int(input("Enter a number: "))

# if a%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# name = str(input("Enter your name: "))
# age = int(input("Enter your age:"))

# if age>=18:
#     print(f"Hello {name} you are a valid voter")
# else:
#     print(f"Hello {name} you are not a valid voter")

# a = int(input("Enter a year: "))

# if a%4 == 0:
#     print(f"{a} is a leap year")
# else:
#     print(f"{a} is not a leap year")

# n = int(input("Enter a number: "))

# for i in range(n,n*10+1,n):
#     print(i)

# for i in range(1,21):
#     if i==1000:
#         print("This is inside if block")
#         break
#     print(i)

# else:10
#     print("This is inside else block")

# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i

# print(f"your sum is {sum}")


# n = int(input("Enter a number: "))

# factorial = 1

# for i in range(1,n+1):
#     factorial *= i


# print(factorial)

# n = int(input("Enter a number: "))
# sum_even = 0
# sum_odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         sum_even += i

#     else:
#         if (i%2 != 0):
#             sum_odd +=i

# print(f"Sum of even numbers is {sum_even} and sum of odd numbers is {sum_odd}")

# n = int(input("which number factors you want: "))

# for i in range(1,n+1):
#     if(n%i==0 and n%n==0):
#         print(i)

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n):
#     if n%i ==0:
#         sum = sum+i

# if sum == n:
#     print("Your numner is perfect")
# else:
#     print("Not a perfect number")


# n = int(input("Enter a number: "))

# count = 0 

# for i in range(1,n+1):
#     if n%i==0:
#         count = count + 1

# if count == 2:
#     print("Number is prime")

# else:
#     print("Number is not prime")
   


# a = "SHREYANS"
# b= ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print (b)


# a = str(input("Enter a string: "))
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b += a[i]

# if b == a:
#     print("Your string is palindrome")
# else:
#     print("Its not a palindrome")


# a = str(input("Enter a string: "))
# char = 0
# dig = 0
# spc = 0
# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spc +=1
# print(f"your string is{a}")
# print(f"Your digits are {dig}\n your alphabets are {char}\n your special characters are {chr}\n")


# a = int(input("Enter a number: "))

# rev = 0
# copy = a

# while a > 0:
#     rev = rev * 10 + a%10
#     a = a//10

# if copy == rev:
#     print("Its a palindrome")
# else:
#     print("Not a Palindrome")

# import random

# num = random.randint(1,11)

# tries = 0

# while True:
#     guess = int(input("Please enter your number: ")) 

#     if num == guess:
#         tries +=1
#         print(f"You are right, you guessed the number in {tries} tries")
#         break

#     elif num<guess:
#         print("Go a little lower")
#         tries+=1

#     elif num>guess:
#         print("Go a little higher") 
#         tries+=1
    

#     else:
#         tries +=1
#         print("Sorry you are wrong")


# def sum(a,b,c):
#     print(f"The sum of your numbers is {a+b+c}")

# sum(12,52,20)
# sum(20,20,20)


# def hello(name,age):
#     print(f"Your name is {name} and age is {age}")

# hello(age = 22, name = "sid")

# def sum(a,b=45):
#     print(f"The sum is {a+b}")

# sum(12,34)

# def Palindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

# Palindrome("NAMAN")
# Palindrome("CURSOR")


# def hello():
#     return "i am good"

# print(hello())


# a = [12,13,15,24]

# a[1] = 29

# print(a[1])
# print(a)

# a = [12,13,14,15,19]

# for i in range(len(a)):
#     print(a[i])

# print(dir(list))

# help(list)

# l = [-1,2,-3,4,5,-6,7,-8,9]

# for i in l:
#     if i >= 0:
#         print(f"Positive elements are: {i}")


# for i in l:
#     if i<0:
#         print(f"Negative elements are: {i}")

# a = [1,2,3,4,5,6,7,8]

# largest = a[0]
# second_largest = a[0]

# for i in a:
#     if i > 0:
#         second_largest = largest
#         largest = i
#     elif i > second_largest:
#         second_largest = i

# print(second_largest)
# print(largest)

# a = [12,13,14,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue

#     else:
#         print("Your list is not sorted")
#         break

# else:
#     print("Your list is sorted")
        

# a = (1,2,3,4,5,5,5,5,5,6)

# b = a.count(5)
# print(b)

# a,b,c,d = (1,2,3,4)

# print(c)


# a = {1,8,"hello",9,2,4,5,6}

# for i in a :
#     print(i)

# a = {1,2,3,4}
# b = {4,5,6,7,8}

# b-= a 

# print(b)

# d = {10:100,20:200,30:300,40:400}

# a = [1,2,3,4,5]

# b = a.copy()

# b[0] = 100
# print(a)


# a = [1,2,3,4,5]

# b = a.copy()

# b[0] = 100

# print(a)
# print(b)


# d = {1:100,2:200,3:300,4:400}

# d2 = d.copy()

# d2[1] = 1000

# print(d2)
# print(d)

# d = {1:100,2:200,3:300,4:400}

# d2 = d.update({5:500})

# d2 = d.copy()

# print(d2)

# d1 = {1:100,2:200,3:300,4:400,5:300}

# d2 = {5:500,6:600,7:700,8:800}

# for i in d2:
#     d1[i] = d2[i]


# print(d1)


# d = {1:100,2:200,3:300,4:400}

# sum = 0
# for i in d:  
#     sum = sum + d[i]

# print(sum)

a = [1,1,1,2,2,2,2,3,3,4,4,4,4,4,4,4,5,6,6,6,7,8,9]

dict = {}

for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

print(f"Your unique elements are {list(dict.keys())}")