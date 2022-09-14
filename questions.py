# To create a guessing game, we need to write a program to select a random number between 1 and 10. To give hints to the user, 
# we can use conditional statements to tell the user if the guessed number is smaller, greater than or equal to the randomly selected number.

import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
      
print("you guessed it right!!")

# calculate mean median mode

# Mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean)

# Median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)

# Mode
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)

                                                                        # RANGE 
for i in range(3)

range(3) gives you a list that starts at 0 and ends at 2. Therefore, its result is [0,1,2]. Combined with the loop, in each iteration, 
i will have the following values: 0 in the first iteration, then 1 in the second and finally 2 in the last/third iteration.

Now, let’s say we have a list my_list = ['a', 'b', 'c']. And then we write: for c in my_list: In this case, as before, 
        c will iterate through my_list and changing its value in each iteration, starting with "a", then "b" and finally "c".

It should be clear now what happens if you were to write: for i in range(len(my_list))

The len() will pass its result - which is 3 - as an argument to the function range(). So it is the same as our first loop which had range(3). 
This is very useful when you want to modify the list at certain positions. To make a mabye not so useful illustration:

my_list = ['a', 'b', 'c', 'd', 'e' ]
for index in range(len(my_list)):
    if my_list[index] in 'aeiou':
        my_list[index] = 'vowel'
    else:
        my_list[index] = 'consonant'

my_list == ['vowel' 'consonant', 'consonant', 'consonant', 'vowel' ] #true
Concluding that:

for i in range() iterates through numbers. for element in my_list iterates through whatever is in the list
(they could be numbers, too) for i in range(len(a_list)) iterates through numbers (which can be used for index access of a_list).


When To Use Method 2 — for element in a list
We use this when we have no need for the index of the elements inside the list. For instance:

Finding the sum of odd numbers in a list:

lis = [1,2,3,4,5,6]
total = 0
for number in lis:
    if number%2==1:
        total += number
        
Finding sum even numbers

sum=0
for i in list3:
  if i % 2==0:
    sum=sum+i
print(sum)
        
Finding squares of numbers in a list:

lis = [1,2,3,4,5,6]
output = []
for number in lis:
    output.append(number**2)
    
When To Use Method 1 — for i in range(len(list))
We use this method when we need the index of the elements — especially when we need more than 1 index per iteration. For instance:

Finding the sum of consecutive numbers:

lis = [1,10,100,1000,10000]
output = []
for i in range(len(lis)-1):
    this = lis[i]
    next = lis[i+1]
    output.append(this+next)
# [11,110,1100,11000]
Combining consecutive strings together:

lis = ["apple", "orange", "pear", "durian"]
output = []
for i in range(len(lis)-1):
    this = lis[i]
    next = lis[i+1]
    output.append(this + " " + next)
# ["apple orange", "orange pear", "pear durian"]
Finding numbers smaller than both left & right neighbours:

lis = [5,3,4,6,2,7,1,8]
output = []
for i in range(len(lis)-2):
    left = lis[i]
    this = lis[i+1]
    right = lis[i+2]
    if this < left and this < right:
        output.append(this)
# [3,2,1]
These problems can only be solved using method 1 
(for i in range(len(list))) but not method 2 (for element in list), as we must have the index of each element to get 
more than 1 element at each iteration.

