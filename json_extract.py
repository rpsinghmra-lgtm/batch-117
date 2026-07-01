import json
with open("product.json","r") as file:
    a=json.load(file)
    with open("clean.txt","w") as file:
        for i in a:
            file.write(f"\n{i}:{a.get(i)}")