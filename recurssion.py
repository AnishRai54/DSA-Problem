# print names n times
def display_name(str,n):
    count=0
    if count==n:
        return
    print(str)
    count+=1
    display_name(str,n-1)

# display_name('Anish',6)


# pirnt 1 to n using recursion

def arange(i,n):
    if i>n:
        return
    print(i)
    arange(i+1,n)
# arange(1,5)

# print n to 1

def display(i,n):
    if i<1:
        return
    print(i)
    display(i-1,n)
# display(5,1)

#sum of first n  number

# def sum(i,total=0):
#     if i<1:
#         print(total)
#         return
#     sum(i-1,total+i)

# sum(5)

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

# print(sum(5))


# factorial using recursion

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

# print(fact(5))

# reverse an array

def reverse_arr(arr):
    start=0
    end=len(arr)-1
    if start>=end:
        return
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start+=1
    end=end-1
    return arr


# fibonnaci using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(5))

    


































#