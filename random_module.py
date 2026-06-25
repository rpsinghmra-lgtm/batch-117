import random
# it worls on iterators
# list=["aman","kamal","shivam","anshu"]

# res=random.choice(list)
# print(res)

# list22=["aman","kamal","shivam","anshu"]
# weight=[2,3,1,0]
# res=random.choices(list22,weights=weight,k=1)
# print(res)
# list22=["aman","kamal","shivam","anshu"]
# weight=[2,3,1,0]
# res=random.choices(list22,weights=weight,k=4)
# print(res)
# res=random.random()*10000
# print(int(res))
# res=random.random()*100
# print(int(res))
# res=random.random()*1008
# print(int(res))
# rand_int=random.randint(1,10)
# rand_range=random.randrange(1,10)
# print(rand_int)
# print(rand_range)
#user max attmpt = 6
#each attempt random number generate
# fix_value=150
# sum=0
# for i in range(6):
#     num=random.randint(24,26)
#     sum+=num
# print(sum)
# if sum==150:
#     print("sum is matched:",sum)
# elif sum>140 and sum<160:
#     print("sum is nearest:",sum)
# elif sum>100 and sum<200:
#     print("sum is far:",sum)
# else:
#     print("sum is farthest:",sum)

# sample()
# shuffle()
#list22=["aman","kamal","shivam","anshu"]
#res=random.sample(list22,k=2)
#print(res)
#random.shuffle(list22)
#print(list22)
# coupon code
# CXYZ6755
# def generate_coupon():
#     a_to_z="abcdefghijklmnopqrstuvwxyz"
#     num="1234567890"
#     char=[random.choice(a_to_z).upper() for i in range(1,5)]
#     num=[random.choice(num) for i in range(1,5)]
#     print("".join(char+num))
# for i in range(1,10):
#     generate_coupon()
# def generate_coupon():
#         a_to_z="abcdefghijklmnopqrstuvwxyz"
#         num="1234567890"

#         char="".join(random.choices(a_to_z,k=4))
#         num=random.random()*10000

#         res=char.upper()+str(int(num))
#         print(res)
    
# for i in range(1,10):
#     generate_coupon()
    
# def generate_code():
#     import string
#     "".join(random.choices(string.ascii_uppercase,k=4))
#     +"".join(random.choices(string.digits,k=4))

# for i in range(1,10):
#     generate_code()
# def generate_coupon():
#      a_to_z="abcdefghijklmnopqrstuvwxyz"
#      num="1234567890"

#      char="".join(random.choices(a_to_z,k=4))
#      num=random.random()*10000

#      res=char.upper()+str(int(num))
#      print(res)
# for i in range(1,10):
#      generate_coupon()
import random
def generate_coupon():
    import string
    coupon=(
    "".join(random.choices(string.ascii_uppercase ,k=4))
    + "".join(random.choices(string.digits ,k=4))
    )
    return(coupon)

for i in range(1,10):
    print(generate_coupon())
