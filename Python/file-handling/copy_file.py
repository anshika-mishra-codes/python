def copy_file(source_file,des_file):
    with open(source_file,"r") as file:
        data= file.read()

    with open(des_file,"w") as f:
        f.write(data)
copy_file("student.txt","backup.txt")