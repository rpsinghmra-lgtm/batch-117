import pymysql 
import json
import pandas as pd
mysql_connection=pymysql.connect(user="root",host="localhost",password="Rpsingh@123")
agent=mysql_connection.cursor()
user_db=input("enter db name")
try:
    agent.execute(f"create database {user_db}")
    print("database created")
    agent.execute("show databases")
    print(agent.fetchall())
except Exception as e:
    print(e)
try:
    agent.execute(f"use {user_db}")
    user_tb=input("enter table name")
    agent.execute(f"create table {user_tb} (id int,title text,description text,category varchar(200),price float,discountPercentage float,rating float,stock int)")
    print("table created succesfully")
    with open("product.json2","r") as f:
        data=json.load(f)
        agent.execute(f"""INSERT INTO {user_tb} VALUES(
                            {data["id"]},
                            '{data["title"]}',
                            '{data["description"]}',
                            '{data["category"]}',
                            {data["price"]},
                            {data["discountPercentage"]},
                            {data["rating"]},
                            {data["stock"]}
                            )""")
        print("data entered successfully")
        agent.execute(f"select * from {user_tb}")
        res=agent.fetchall()
        ab=pd.DataFrame(res,columns=['id','title','description','category','price','discountPercentage','rating','stock'])
        print(ab)
except Exception as e:
    print(e)


