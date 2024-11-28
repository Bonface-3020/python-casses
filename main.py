#open file
file=open('sample.txt')
#read file
print(file.read())
file.close()

#open in write mode
file_write=open('sample.txt','w')
file_write.write("haloo, my name is AYOBAMI")
file_write.close()