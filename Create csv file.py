#create a csv format file
#with user input specifying name and age
#write the file to a location 


#declare variables
file_name='names3.csv'
WRITE='w'
READ='r'
APPEND='a'
READWRITE='w+'

#Programme will work with a semicolon, not a comma as a seperator

name=input("Enter name and age (Thabo; 56): ")
#actual file
file=open(file_name,WRITE)
file.write(name)

print("file written")

file.close()