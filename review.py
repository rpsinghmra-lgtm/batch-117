# sentimental analysis
review=[
    {"negative":"this is very bad product i ordered one month ago",
    "positive":"this product is very nice go for it",
    "bad_products":["Shoes","Cricket Bat"],
    "good_products":["Books","Mobile phone"]
    },
]
import pymysql
import pandas as pd
mysql_connection=pymysql.connect(user="root",host="localhost",password="Rpsingh@123")
print(mysql_connection)
# ravi=mysql_connection.cursor()
# my_db=input("enter my db name")
# try:
#     ravi.execute(f"create database {my_db} ")
#     print("database created")
#     print(ravi.fetchall())
# except Exception as e:
#     print(e)

# try:
#     ravi.execute(f"use {my_db} ")
#     my_table=input("enter table name")
#     ravi.execute(f"create table {my_table} (review[0][0] text,review[0)[1] text,review[0][2] varchar(255),review[0][3] varchar(255)")
#     print("table created sucessfully")
# except Exception as e:
#     print(e)
# for i in review:
#     for key in i.keys():
#         print(key)
#     query=f"CREATE TABLE IF NOT EXIXTS PRODUCT_REVIEW"
#     {key}

