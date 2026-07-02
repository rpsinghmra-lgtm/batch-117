import pymysql
import json
import pandas as pd

with open("table.json")as f:
    schema=json.load(f)

with open("student_profile.json")as f:
    student_schema=json.load(f)

mysql_db=pymysql.connect(user="root",host="localhost",password="Rpsingh@123")
ravi=mysql_db.cursor()
    
db_name=schema['database']
ravi.execute(f"create database if not exists {db_name}")
print(f"database '{db_name}' created successfully")

ravi.execute(f"use {db_name} ")

col_definition=",".join([f"{col} {dtype}" for col,dtype in schema["columns"].items()])
ravi.execute(f"create table if not exists {schema['table_name']} ({col_definition})")
print("table created using json schema")


row_definition=student_schema["students"]

for i in row_definition:
    ravi.execute(f"""insert into {schema['table_name']}
                 (id,first_name,role,age,email,phone)
                 values (%s,%s,%s,%s,%s,%s)""",
                 (
                    i["id"],
                    i["name"],
                    i["role"],
                    i["age"],
                    i["email"],
                    i["phone"]
                 )
    )


mysql_db.commit()
print("data inserted successfully")
