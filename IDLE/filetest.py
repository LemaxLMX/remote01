file=open('1.txt','rb')
print(file.readline().decode().strip())
file.seek(3,1)
print(file.readline().decode().strip())

for line in file:
  print(line.decode(),end="")

file.close()
