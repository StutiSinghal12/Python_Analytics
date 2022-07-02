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

