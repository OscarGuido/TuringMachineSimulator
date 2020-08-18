#########################################################
### Simulador de una Maquina de Turing de una Cinta.  ###
### Oscar Guido Delgado.                              ###
### 22 de mayo de 2020.                               ###
#########################################################

import sys
import time
import os

segundos=1 #Tiempo de espera en segundos

def crea_maquina(archivo):
	transiciones=[]
	f = open(archivo,'r')
	linea=1
	separador=","
	for cadena in f.readlines():
		if linea==1:
			if cadena[-1] == '\n':
				cadena = cadena[:-1]			
			edo_inicial=cadena
		elif linea==2:
			if cadena[-1] == '\n':
				cadena = cadena[:-1]
			edos_finales=cadena.split(separador)
		else:
			if cadena[-1] == '\n':
				cadena = cadena[:-1]
			transicion=cadena.split(separador)
			transiciones.append(transicion)	
		linea+=1
	f.close()
	return edo_inicial, edos_finales, transiciones

def reemplaza(cadena,i,caracter):
	mi_cadena=""
	mi_cadena+=cadena[:i]
	mi_cadena+=caracter
	mi_cadena+=cadena[i+1:]
	return mi_cadena

def imprime_pantalla(cadena_inicial, estado, cadena,i,t):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Cadena original: ", cadena_inicial)
	print("\n")	
	print("Estado actual: ", estado,"\n")	
	espacios=""
	x=0
	while x<i:
		espacios+=" "
		x+=1
	espacios+="^"	
	print("\t",cadena)
	print("\t",espacios)
	print("\n")	
	print("δ(", t[0],",", t[1],") = (",t[2],",",t[3],",",t[4],")")
	time.sleep(segundos)

def rellena_cadena(cad):
	l=len(cad)
	y=0
	blanco=""
	while y<=l:
		blanco+="#"
		y+=1

	cadena=blanco
	cadena+=cad
	cadena+=blanco
	return cadena,y

#Inicio del programa.
archivo=sys.argv[1]
edo_inicial, edos_finales, transiciones = crea_maquina(archivo);
edo_actual=edo_inicial
cad = input("Cadena a analizar: ")
cadena,y=rellena_cadena(cad)
cadena_inicial=cadena

i=y
while i<len(cadena):	
	flag=False
	for t in transiciones:
		if edo_actual==t[0] and cadena[i]==t[1]: #Se encuentra la transicion correcta
			imprime_pantalla(cadena_inicial,edo_actual,cadena,i,t)		
			edo_actual=t[2]
			flag=True
			cadena=reemplaza(cadena,i,t[3])
			imprime_pantalla(cadena_inicial,edo_actual,cadena,i,t)
			if t[4]=='R' or t[4]=='r':
				oxxo=1
			elif t[4]=='L' or t[4]=='l':
				i-=2
			elif t[4]=='-':
				i-=1
			else:
				print("Simbolo ", t[4], " no ha sido reconocido")
			break
	if flag==False:	
		print("\nTransicion δ(", edo_actual,",", cadena[i],") no definida")
		break	
	i+=1

if edo_actual in edos_finales:
	print("\nMT termino en un estado de aceptacion (", edo_actual, ")\n")
else:
	print("\nMT NO termino en un estado de aceptacion (", edo_actual, ")\n")

print("Cadena original: ", cadena_inicial)
print("Cadena final:    ", cadena)
