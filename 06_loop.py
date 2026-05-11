# while loop

# i=1
# while i <= 5:
#     print("krish")
#     i = i+1

# #while loop practice set

# i=1
# while i <=100:
#     print(i)
#     i = i+1

# i=100
# while i >=1:
#     print(i)
#     i = i-1

# t=int(input("enter the number"))
# i=1
# while i <=10:
#     print(t," + ",i," = ",t*i)
#     i = i+1

# l=[]
# s=1
# while s <=10:
#     l.append(s*s)
#     s=s+1

# print(l)

# a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# while i < len(a):
#     print(a[i])
#     i = i+1

# a=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100,81)
# x=81
# i=0
# while i < len(a):
#     if a[i] == x:
#         print(a[i],"found")
#     else:
#         print(a[i])
#     i = i+1

# i=1
# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i = i+1

# i=1
# while i <= 5:
#     if i==3:
#         i=i+1
#         continue
#     print(i)
#     i = i+1

# i=1
# while i <= 10:
#     if i%2==0:
#         print(i)
#     i = i+1 

# for loop

# i=[1,2,3,4,5,6,7,8,9,10]
# for x in i:
#     print(x)

# str="krish"
# for x in str:
#     print(x)

# i=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# f=81
# for x in i:
#     if x == f:
#         print(x,"found")
#     else:
#         print(x)

# for i in range(5):
#     print(i)

# for i in range(1,11):
#     print(i)

# odd numbers
# for i in range(1,10,2):
#     print(i)

# even numbers
# for i in range(2,11,2):
#     print(i)


# for i in range(100,0,-1):
#     print(i)

for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()



