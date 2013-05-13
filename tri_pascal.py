def tri_pascal(n):
	if n == 0:								#Caso base: grado 0 = 1
		return [1]
	else:
		retorno = []						#Lista de coeficientes (vacia, se concatenan nuevos coef)
		for i in range(n+1):
			if i == 0 or i == n:			#Si tratamos con primer o ultimo termino, agregar 1
				retorno = retorno + [1]
			else:							#Sino calculamos con los numeros superiores en triangulo (notar indices)
				retorno = retorno +[tri_pascal(n-1)[i-1]+tri_pascal(n-1)[i]]
		return retorno

