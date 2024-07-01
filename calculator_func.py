#The proposed calculator works on any number of inputs given in the form of a list
#adds up all the numbers in the list
import math
def add(a):
    result=0
    for i in a:
        result+=i
    return result


# subtracts all the subsequent numbers from the first number of the list
def subtract(a):
    result=a[0]
    for i in range (1,len(a)):
        result-=a[i]
    return result


# returns product of all numbers of the list
def multiply(a):
    result=1
    for i in a:
        result*=i
    return result


# divides the first number by the second number and the result by the third and so on..
def divide(a):
    result=a[0]
    for i in range (1,len(a)):
        result/=a[i]
    return result


# returns the mean value of a list
def mean(a):
    return add(a)/len(a)


# outputs the median of a list
def median(a):
    a.sort()
    n=len(a)
    if (n%2==0):
        return (a[n/2]+a[n/2-1])/2
    else:
        return a[n//2]
    
    
# returns the standard deviation for a given set of numbers
def sd(a):
    result=0
    for i in a:
        result+=(i-mean(a))**2
    return math.sqrt((result)/len(a))


# this is a helper function returning output on only two integers
def gcd1(a,b):
    r=a%b
    while (r!=0):
        a=b
        b=r
        r=a%b
    return b


# returns the greatest common divisor of all the numbers
def gcd(a):
    i=0
    while (len(a)!=1):
        a[i:i+2]=[gcd1(a[i],a[i+1])]
    return a[0]


# returns the least common multiple of all the numbers
def lcm(a):
    i=0
    while (len(a)!=1):
        a[i:i+2]=[a[i]*a[i+1]/(gcd1(a[i],a[i+1]))]
    return a[0]


# output the factorial of an integer and is a helper function
def fact(n):
    result=1
    i=1
    while (i<=n):
        result*=i
        i+=1
    return result


# outputs the factorial of all the numbers in the list
def fact_nums(a):
    n=len(a)
    for i in range (n):
        print(fact(a[i]), end=' ')