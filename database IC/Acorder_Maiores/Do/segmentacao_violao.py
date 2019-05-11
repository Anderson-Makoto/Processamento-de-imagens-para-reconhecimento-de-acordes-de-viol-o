from glob import glob
import os

diretorios= glob('C:/Users/makoto/Desktop/database IC/Acorder_Maiores/*/')

nome= []
cont= 0
for i in (diretorios):
    for j in range(len(i)):
        if i[j: j+ 1]== '\\':
            nome.append(i[j+ 1:len(i)- 1])

for i in range(int(len(nome)/ 2)):
    print(i)
    nome.remove('')
    
print(nome)

