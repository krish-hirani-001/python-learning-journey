# def ave(a,b,c):
#     print("average of a , b or c = ",(a+b+c)/3)

# ave(5,10,10)

# default value pass

# def multi(a=10,b=20):
#     print(a*b)
# multi() # multi(3,5) argu provied so output is 15 

# a=["a",1,3,5,6,8,9,0,3]
# def lenth(l):
#     print(len(l))
# lenth(a)


# a=["a",1,3,5]
# def abc(l):
#     for i in l:
#         print(i,end=" ")
# abc(a)

# a=10
# def factorial(l):
#     a=1
#     for i in range(1,l+1):
#         a =a * i
#     return a
# print(factorial(a))

# a=int(input("enter the amount in USD: "))
# def usd_to_inr(l):
#     i=l*94.426
#     return round(i,2)
# print(f"{usd_to_inr(a):.2f}")
# print(usd_to_inr(a))

# a=int(input("enter a number :"))
# def evenodd(l):
#     if(l%2==0):
#         print("the number is even..")
#     else:
#         print("the number is odd..")
# evenodd(a)


# recursion function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(3)

def suma(a):
    if (a == 0 or a == 1):
        return 0
    
    return suma(a-1) +a
c=suma(11)
print(c)