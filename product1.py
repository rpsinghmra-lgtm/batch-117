import pymysql
import json
import pandas as pd
mysql_connection=pymysql.connect(user="root",host="localhost",password="Rpsingh@123")
ravi=mysql_connection.cursor()
my_db=input("enter db name")
try:
    ravi.execute(f"create database {my_db}")
    print("database created")
    ravi.execute("show databases")
    print(ravi.fetchall())
except Exception as e:
    print(e)

try:
    ravi.execute(f"use {my_db}" )
    my_table=input("enter table name")
    ravi.execute(f"create table {my_table} (rating int,comment text,reviewerName text,reviewerEmail text)")
    print("table created successfully")
    with open("product.json3","r") as f: 
        data=json.load(f)
        ravi.execute(f"""INSERT INTO {my_table} VALUES (
                           {data["rating"]},
                           '{data["comment"]}',
                           '{data["reviewerName"]}',
                           '{data["reviewerEmail"]}'
                           )""")
        print("data entered ssuccessfuly")
        ravi.execute(f"select * from {my_table}")
        res=ravi.fetchall()
        ab=pd.DataFrame(res,columns=["rating","comment","reviewerName","reviewerEmail"])
        print(ab)
except Exception as e:
    print(e)