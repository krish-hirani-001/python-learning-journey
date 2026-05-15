# f = open("demo.txt",'w')
# f.write("python file handling topic")
# f.write("\npython is most Popular language in the world")
# f.close()

# fr=open("demo.txt",'r')
# print(fr.read())
# fr.seek(0)
# print(fr.read(5))
# fr.seek(0)
# print(fr.readline())
# fr.seek(0)
# print(fr.readlines())
# fr.close()
 

# f = open("demo.txt",'a')
# f.write("\npython")
# f.close()


# f = open("data.txt","w")
# f.write("my name is hirani krish \nI am study at atmiya university \n")
# f.write("I am learning python language \npython is easy language")
# f.close()

# practice set

# with open("data.txt",'r') as f:
#     data = f.read()
#     new_data = data.replace("python","java")    
#     print(new_data)

# with open("data.txt",'w') as f:
#     f.write(new_data)


# with open("data.txt",'r') as f:
#     data = f.read()
#     new_data=data.find("learning")
#     if(new_data == -1):
#         print("keyword is not exists")
#     else:
#         print("keyword is exists & index nuber :",new_data)