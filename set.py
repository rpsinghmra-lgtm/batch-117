# -----------set--------
# set is a data structure used to store unique values an culry {}
# seta are mutable in nature
#bsets does not support 
# sets always reconize unique value
#indexing and slicing not allowed
# in built methods
# add()
# intersect()
#difference()
# subset()
# union()
#set1={2,3,5,7,6,8}
#set2={3,5,7,9,10}
#res1=set1.union(set2)
#print(res1)
#res2=set1.intersection(set2)
#print(res2)
#res3=set1.issubset(set2)
#print(res3)
#set1.add(87)
#print(set1)
# res1=set1.difference(set2)
# print(res1)
# res2=set2.difference(set1)
# print(res2)
# set1={2,3,5,7,6,8}
# set2={2,3,5}
# res=set2.issubset(set1)
# print(res)
set1={2,3,5,7,6,8}
#set1.add(2)
set1.update([45,54,65])
set1.update({33,44,555})
print(set1)
