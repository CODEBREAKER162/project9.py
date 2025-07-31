#File managing :
'''In file  Managing its like managing a file 
-->Opening the file 
-->Reading the file 
-->Closing the file 
In this  you have to example'''


# file = open("notes.txt","w")
# file.write("Hello world \n I am robot for human needs in good way")
# file.close()


# file = open("notes.txt","r")
# content = file.read()
# print(content)
# file.close()

file = open("www.hppt","w")
file.write("Hello World!\n This is new to me ")
file.close()
file = open("www.hppt","r")
content = file.read()
print(content)
file.close()
'''| File Mode | Use                                 |
| --------- | ----------------------------------- |
| `"r"`     | Read file (must exist)              |
| `"w"`     | Write file (overwrites old content) |
| `"a"`     | Append to file (adds to end)        |
| `"x"`     | Create file (error if exists)       |
| `"r+"`    | Read and write                      |
'''

