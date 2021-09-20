#part 3
file = input("Enter the name of file: ")
e=open(file,'w')
store_file = input("Enter the contents to be stored in a file: ")
e.write(store_file)
e.close()