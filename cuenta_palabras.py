def cuenta_palabras(diccionario):
	if len(diccionario) == 0:						#Caso base: diccionario vacio = 0
		return 0
	else:
		datos = list(diccionario.items())[0]		#Tupla con "primer" item del diccionario
		aux = diccionario.copy()					#Copia del diccionario (evita alteraciones al original)
		aux.pop(datos[0])							#Elimina elemento ya guardado en variable datos
		return datos[1] + cuenta_palabras(aux)		#Cantidad de datos mas lo obtenido de aux