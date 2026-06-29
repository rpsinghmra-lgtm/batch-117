#----------file handling-------------
#file handling in python meand reading from and writing to files/folder stored on
# disk using python

#2 your python code can open a file,pull out data of it,put data into it and
# also close it properly

#-----------what is file
# files are store of data and information on the specific path to divice

# types of files
#1.text file (.txt,.csv,.json)
#2.binary files(images,videos,audio)

# types of file path.
#1.absolute path : the complete path from the root of the filesystem.
#2.relative path : the path relative to where your current folder (current,working dir)

# file mode
#1.a :append,a+ :append and read
#2. w : write, w+ : write and read
# 3. r : read, r+ : read and write
#4.x : srictally create file

# python file handling methods.
#1.open(file_name_mode):open file
#2.close():close file
#3.flush():memory cleanup.

#4.read() : file read
#5.readlines():file read line by lines.
#6.write(): write data in file only take settings.
# write data in file of any types.

#8.tail(): cursor move
# 9.seek(): specific position set of cursor
# 
# 
#1.creeate a file in strict mode
#file=open("strict.txt","x")
#print("file created..")
# try:
#     file=open("strict.txt","x")
#     print("file created..")
# except Exception as e:
#     print("error:  file already exists")
# file=open("strict.txt","w")
# file.write("this is python file handling...")
# file.write("/nwhat about your coding")
# file.flush()
# file.close()

# context manager
# with open("manager.txt","w+") as f:
#     f.write("this is proper python file handling")
#     f.seek(0)
#     f.read()
#     print("file created and ritten")
with open("demo.txt","w+")as f:
    f.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
             Lorem Ipsum has been the industry's standard dummy text ever since 1966,
             when designers at Letraset and James Mosley,
             the librarian at St Bride Printing Library in London,
             took a 1914 Cicero translation and scrambled
             it to make dummy text for Letraset's Body Type sheets.
             It has survived not only many decades
            , but also the leap into electronic typesetting, remaining essentially unchanged.""")
    f.seek(0)
    r=f.read()
    # print(r)
    numbers=" "
    for i in r:
        if not i.isdigit():
            numbers+=i
    print(numbers)
    with open("modify_demo.txt","w") as f:
        f.write(numbers)


    
