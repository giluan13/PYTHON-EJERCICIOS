import os
os.system

print("")
num_segundos=int(input("Digite un numero expresando en segundos"))

dias=((num_segundos//60)//60)//24
hora=((num_segundos//60)//60)%24
minutos=(num_segundos//60)%60
segundos=num_segundos%60

print("dias: ",dias)
print("horas: ",hora)
print("minutos: ",minutos)
print("segundos: ",segundos)
print("") 
