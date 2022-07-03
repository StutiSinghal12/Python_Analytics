ques--> max of 3 numbers

def max(a,b,c):
  if a>b and a>c:
    print("max is {}".format(a))
  elif c>a and c>b:
    print("max is {}".format(c))
  else:
    print("max is {}".format(b))
  
print("enter numbers")
a,b,c=(int(input()),int(input()),int(input()))
max(a,b,c)


ques---> find sum

def sum(a,b,c,d):
  s=0
  s=a+b+c+d
  return s
  
  
print("enter numbers")
a,b,c,d=(int(input()),int(input()),int(input()),int(input()))
print("sum is",sum(a,b,c,d))

or 

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

ques--->reverse a string

def reverse(s):
  rev=''
  rev=''.join(reversed(s))
  return rev
  
s='stuti'
print(reverse(s))

question-->calculate factorial

def factorial(n):
  if n==0:
    return 1 
  else:
    return n*(n-1)
    
inp=int(input("enter the number"))
print("factorial is:",factorial(inp))

question--see if n is in range or out of range

def test(n):
  if n in range(3,9):
    print(" number is in range",format(n))
  else:
    print("outside range")
    
test(12)

# list of first 100 positive odd natural numbers using list comprehension.

for i in range(0,100):
  if i%2!=0:
    print(i, end = " ")
    
by list comprehension :-
  
 def odd_numbers(n):
    return [x for x in range(0, n) if x%2 != 0]

print(odd_numbers(100))

# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
  
  
# we can also print odd no's using lambda exp. 
odd_nos = list(filter(lambda x: (x % 2 != 0), list1))
  
print("Odd numbers in the list: ", odd_nos) 


