prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta=[14,23,15,14,12,41,39]
for j in range(0,len(prenume)) :
 print(prenume[j], 'are varsta de', varsta[j])

prenume.append('Andreea')
print(prenume)
prenume.append('Ioan')
print(prenume)
varsta.append('34')
print(varsta)
varsta.append('23')
print(varsta)
del prenume[2:3]
print(prenume)
del varsta[2:3]
print(varsta)
print(prenume[0:3])
print(prenume[::-1])
print('elementele cu indicii 2 sunt', prenume[2], varsta[2])
p=prenume[0:5]
print('elementele cu indicii 4 sunt', prenume[4], varsta[4])
v=varsta[0:5]
print('elementele din ambele liste de la 0 la 5 sunt', p,v)

