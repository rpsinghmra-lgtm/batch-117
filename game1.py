import random
items=["rock","paper","scisor"]
option=(random.choice(items)) 
user_input=input("""
            chose rock or paper or scisor
""")
print(user_input)
print(option)
count_com=0
count_user=0
for i in range(3):
    if option==user_input:
        print("tie")
    elif user_input=="rock" and option=="paper":
        count_com+=1 
        print("computer score is::",count_com)
    elif user_input=="rock" and option=="scisor":
        count_user+=1
        print("user score is:",count_user)
    elif user_input=="paper" and option=="rock":
        count_com+=1
        print("computer score is:",count_com)
    elif user_input=="paper" and option=="scisor":
        count_user+=1
        print("user score is:",count_user)
    elif user_input=="scisor" and option=="rock":
        count_com+=1
        print("computer score is:",count_com)
    elif user_input=="scisor" and option=="paper":
        count_user+=1
        print("user score is:",count_user)
if count_com==count_user:
    print("match tied")
elif count_com>count_user:
    print("computer won:",count_com)

else:
    print("user won:",count_user)
    

        