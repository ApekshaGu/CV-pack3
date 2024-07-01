def calculator(n):
    # contains a description of what functions the calculator contains and can perform
    if n>0:
        print("You can perform any of the functions mentioned below along with their operation:\nadd(a): adds up all the numbers in the list a\nsubtract(a): subtracts all the subsequent numbers from the first number of the list\nmultiply(a): returns product of all numbers of the list\ndivide(a): divides the first number by the second number and the result by the third and so on..\nmean(a): returns the mean value of a list\nmedian(a): outputs median of the list\nsd(a): returns the standard deviation for a given set of numbers\ngcd(a): returns the greatest common divisor of all the numbers\nlcm(a): returns the least common multiple of all the numbers\nfact_nums(a): outputs the factorial of all the numbers in the list")   
    else:
        print("You can't perform any operation on zero number of inputs")
calculator(5)
