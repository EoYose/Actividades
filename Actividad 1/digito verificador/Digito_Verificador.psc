Algoritmo Digito_Verificador
	Leer rut
	factor <- 2
	suma <- 0
	aux <- rut
	Repetir
		aux1 <- aux-(aux MOD 10)
		digito <- aux-aux1
		suma=suma+(factor*digito)
		factor <- factor+1
		Si factor>7 Entonces
			factor <- 2
		FinSi
		aux <- aux1/10
	Hasta Que aux=0
	resto <- suma MOD 11
	Si 11-resto=10 Entonces
		Escribir "K"
	SiNo
		Si 11-resto=11 Entonces
			DV <- 0
		SiNo
			DV <- 11-resto
		FinSi
		Escribir DV
	FinSi
FinAlgoritmo
