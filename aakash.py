# num = int(input("Enter a number: "))

# l1 = []

# if num == 1:
#     print("1 is not prime")
# elif num >= 2:
#     for i in range(2, num + 1): 
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l1.append(i)
# else:
#     print("Enter a valid number")

# print(l1)

#emp_list=["aman","shivam","shubham","anshu","kamal"]
# emp name indivisual file create txt type
# for i in emp_list:
#     with open(f"{i}" ".txt","w+") as f:
#         f.write("file created")
import os
#print(os.listdir()) #make list of files
# print("current folder:",os.getcwd()) # tells us the current older
# path=r"D:\data science\daily_class_practice"
# os.chdir(path) # change directory
# print("current folder:",os.getcwd()) 
# print(os.path.exists("aman.txt")) # wrong file h to nhi jayega
# emp_list=["aman","shivam","shubham","anshu","kamal"]
# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as f:
#             print(f"{i}.txt file created")
#     else:
#         print(f"{i}-file already exits")
#folder="employees_details"
#os.makedirs(folder)
# for i in emp_list:
#     os.remove(f"{i}.txt")
#     print(i,"removed")
# Task
folder="Employee"
# os.makedirs(folder)
# curr=os.getcwd()
# path=curr+"\\"+folder
# os.chdir(path)
# for i in emp_list:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w") as f:
#             print(f"{i}.txt file created")
#     else:
#         print("file already exists")
# with open("aman.txt","w") as f:
#     f.write("its rpsingh from chambal")
# print(os.getcwd())

# curr=r"D:\data science\daily_class_practice"
# path=curr+"\\"+"Employee"
# print(path)
# os.chdir(path)
# print(os.getcwd())
# with open("aman.txt","w") as f:
    # f.write("this is rpsingh from chambal")
# os.getcwd()
# emp_tple=("rahul","ragini")
# folder="Office"
# # os.makedirs(folder)
# yet=os.getcwd()
# print(yet)
# path1=yet+"\\"+folder
# os.chdir(path1)
# for i in emp_tple:
#     file_check=os.path.exists(f"{i}.txt")
#     if not file_check:
#         with open(f"{i}.txt","w")as f:
#             print(f"{i}.txt file created")
#             f.write("this is rpsingh from data science")
#     else:
#         print("file already exists")
# import random
# import string
# def Employee(folder):
#     yet=os.getcwd()
#     path=yet+"\\"+folder
#     os.chdir(path)
#     print(os.getcwd())
#     file=input("enter your file name")
#     with open(f"{file}.txt","w") as f:
#         Id="".join(random.choices(string.ascii_letters,k=4))+"".join(random.choices(string.digits,k=4))
#         emp_name=input("enteremployee name:")
#         meeting_id="".join(random.choices(string.ascii_letters,k=8))+"".join(random.choices(string.digits,k=8))
#         emp_mail=("enter your mail id")
#         f.write(f"employee name is:,{emp_name}")
#         f.write(f"\nemployee id is:,{Id}")
#         f.write(f"\nmeeting id is:,{meeting_id}")
#         f.write(f"\nemp mail is:,{emp_mail}")
#         print(f"{emp_name},{Id},{meeting_id},{emp_mail} add successfully")
# folder=input("enter folder name:")
# Employee(folder)



   



