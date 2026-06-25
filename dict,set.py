dics={"name":"ram", "class":"data science" ,"add":"delhi","population":"5000","vill_name":"anandpur"}
#print(type(dics))
#print(len(dics))
#for i in dics:
#print(dics.values())
#(dics.items()))
#print(len(dics))
# dics.update({'life':'poor','forest':'green'})
# print(dics)
#print(len(dics))
vowels="aeiou"
for i in dics.values():
    for j in i.lower():
        if j in vowels:
            print(j,end="")