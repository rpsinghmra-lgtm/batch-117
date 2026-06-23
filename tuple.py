#multiple data of diffrent types with coma(,) in round braces
# support indexing,slicing,ordered.
# immutable
#traversing
# ---------creation of tuple
#t1,t2,t3=(39,48,"ravi")
#print(t1)
#print(t2)
#print(t3)
#marks_tuple=(50,55,69,34,89)
#print(marks_tuple[-1])
#print(marks_tuple[::-1])
#1. waf to exract all number grater than 40
#marks_tuple=(50,55,69,34,89)
# def marks_grea(m):
#     new_value=[]
#     for i in marks_tuple:
#         if i>50:
#             new_value.append(i)
#     return new_value
# marks_tuple=(50,55,69,34,89)
# res=marks_grea(marks_tuple)
# print(res)
# waf to sum of all indices of tuple.
# def sum_indices(tuple1):
#     sum=0
#     for i in range(len(tuple1)):
#         sum+=i
#     return sum
# tuple1=(50,55,69,34,89)
# res=sum_indices(tuple1)
# print(res)
#tuple2=(40,50,65,47,43,23,4,54)
#print(len(tuple2))
#print(tuple2[5])
# sum=0
# for i in tuple2:
#     sum+=i
# print(sum)
# for i in tuple2:
#     if i>40:
#         print(i)
# for i in tuple2:
#     if i==2 or i==3:
#         print("number is prime:",i)
#     elif i==0 or i==1 or i%2==0 or i%3==0 or i%5==0:
#         continue
#     else:
#         print("numbers are prime:",i)

# tuple2=(40,50,65,47,43,23,4,54)
# res=tuple(sorted(tuple2))
# print(res)
# tuple2=(40,50,65,47,43,23,4,54)
# res=tuple(sorted(tuple2,reverse=True))
# print(res)
#tuple2=(40,50,65,47,43,23,4,54)
#print(tuple2[::2])
# for i in range(len(tuple2)):
#     if i%2==0:
#         print(tuple2[i])
#     else:
#         continue
# great=tuple2[0]
# for i in tuple2:
#     if i>great:
#         great=i
# print(great)
#print(min(tuple2))
# name=["ram","Shyam"]
# a="".join(name)
# print(a)
# vowels="aeiou"
# for i in a:
#     if i not in vowels:
#         print(i,end="")
# str1="this is python"
# vowels="aeiou"
# for i in str1:
#     if i not in vowels:
#         print(i,end="")
# str1="this is python"
# vowels="aeiou"
# for i in range(len(str1)):
#     if str1[i] in vowels:
#         print(i)
# str1="this-is-python123"
# for i in str1:
#      if i.isdigit():
#          print(i)
# list2=[24,34,56,78,89,87]
# l1=[]
# l2=[]
# for i in list2:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print("even numbers are:",l1)
# print("odd numbers are:",l2)
# list3=["python programming"]
# res=list3[0][::-1]
# print(res)
# list3=["python","programming"]
# res=[i[::-1]for i in list3]
# print(res)
# list2=["python programming"]
# for i in list2:
#     res="".join(list2)
# print(res)
# i in res:
#     res[0],res[-1]==res[-1],res[0]
#     print(res)


print("hello")