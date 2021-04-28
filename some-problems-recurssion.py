### SUM with recurssion

def sumF(n):
    if n == 0:
        return 0
    return n+sumF(n-1)
print(sumF(4))




### Reverse a list of numbers using recurssion
list = [1, 2, 3, 4]

def reverseList(someList):
    if len(someList) == 0:
        return []
    return [someList[-1]]+reverseList(someList[:-1])

print(reverseList(list))


## Recurssive fibonacci

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(6))


