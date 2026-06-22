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
def sum_indices(tuple1):
    sum=0
    for i in range(len(tuple1)):
        sum+=i
    return sum
tuple1=(50,55,69,34,89)
res=sum_indices(tuple1)
print(res)

