from random import *
i = j = soma = 0
secao = []
total =[]
#metodo random para criação das variáveis
for i in range (20):
 secao.append(randint(0,9))

#Organização dos dados por Bubble Sort
for i in range(20):
  for j in range(19):
    if(secao[j] > secao[j+1]):
      aux = secao[j]
      secao[j] = secao[j+1]
      secao[j+1] = aux

#Contagem de Candidatos por seção
count = 0
j=0
while (j<10):
  for i in range (20):
    if(j==secao[i]):
      count = count +1
  total.append(count)
  j = j+1
  count = 0  


#Apresentação dos dados
for i in range (10):
  print ('Secao',i,'-',total[i], 'Candidatos')
 