file = open('testfile.txt','a',encoding="UTF-8") 
 
file.write("Hello World \n")  

file.close() 

file = open("testfile.txt","r",encoding="UTF-8")

print (file.read())

file.close()