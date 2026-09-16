Algoritmo gato_en_raya
	FinalVerdadero = Falso
	//Elegir ficha
	repetir
		auxsalida <- Falso
		Escribir 'elija X o O'
		Repetir
			Leer fichajugador
			fichajugador <- Mayusculas(fichajugador)
			Si fichajugador='X' O fichajugador='O' Entonces
				Si fichajugador='X' Entonces
					fichamaquina <- 'O'
				SiNo
					fichamaquina <- 'X'
				FinSi
				auxsalida <- Verdadero
			SiNo
				Escribir 'Entrada no valida. Por favor elija X o O'
			FinSi
		//Elegir turno
		Hasta Que auxsalida=Verdadero
			auxsalida <- Falso
			Escribir 'Elija su turno:'
			Escribir '(1) Empiezas tu'
			Escribir '(2) Empieza la maquina'
			Repetir
				Leer auxturno
				Si auxturno='1' O auxturno='2' Entonces
					auxsalida <- Verdadero
					turnojugador <- ConvertirANumero(auxturno)
				SiNo
					Escribir 'Entrada no valida. Por favor elija 1 o 2'
				FinSi
		Hasta Que auxsalida=Verdadero
		auxsalida <- Falso
		// Iniciacion de variables
		final <- Falso
		mensajefinal <- ''
		turno <- 1
		victoria <- Falso
		a <- ''
		b <- ''
		c <- ''
		d <- ''
		e <- ''
		f <- ''
		g <- ''
		h <- ''
		i <- ''
		Repetir
			// Jugar
			Si turno=turnojugador Entonces
				Escribir "Es tu turno"
				// Jugador Juega
				Escribir 'A | B | C'
				Escribir '---------'
				Escribir 'D | E | F'
				Escribir '---------'
				Escribir 'G | H | I'
				Escribir 'Indique la posicion en la que jugara'
				Repetir
					Leer posicion
					posicion <- Mayusculas(posicion)
					// Verificacion de jugada Valida
					Según posicion Hacer
						'A':
							Si a='' Entonces
								a <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'B':
							Si b='' Entonces
								b <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'C':
							Si c='' Entonces
								c <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'D':
							Si d='' Entonces
								d <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'E':
							Si e='' Entonces
								e <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'F':
							Si f='' Entonces
								f <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'G':
							Si g='' Entonces
								g <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'H':
							Si h='' Entonces
								h <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						'I':
							Si i='' Entonces
								i <- fichajugador
								auxsalida <- Verdadero
							SiNo
								Escribir 'Casilla ocupada. Por favor use otra'
							FinSi
						De Otro Modo:
							Escribir "Entrada Invalida. Por favor ingrese una letra del tablero."
					FinSegún
				Hasta Que auxsalida=Verdadero
				auxsalida <- Falso
			SiNo
				// Maquina Juega
				Escribir "Es turno de la maquina"
				Si a='' Entonces
					a <- fichamaquina
				SiNo
					Si b='' Entonces
						b <- fichamaquina
					SiNo
						Si c='' Entonces
							c <- fichamaquina
						SiNo
							Si d='' Entonces
								d <- fichamaquina
							SiNo
								Si e='' Entonces
									e <- fichamaquina
								SiNo
									Si f='' Entonces
										f <- fichamaquina
									SiNo
										Si g='' Entonces
											g <- fichamaquina
										SiNo
											Si h='' Entonces
												h <- fichamaquina
											SiNo
												Si i='' Entonces
													i <- fichamaquina
												SiNo
													Escribir 'Error de maquina. mensaje imposible de mostrar'
												FinSi
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			// Detectar Victoria
			Si a=b Y b=c Y a<>'' Entonces
				victoria <- Verdadero
			SiNo
				Si d=e Y e=g Y d<>'' Entonces
					victoria <- Verdadero
				SiNo
					Si g=h Y h=i Y h<>'' Entonces
						victoria <- Verdadero
					SiNo
						Si a=d Y d=g Y a<>'' Entonces
							victoria <- Verdadero
						SiNo
							Si b=e Y e=h Y b<>'' Entonces
								victoria <- Verdadero
							SiNo
								Si c=f Y f=i Y c<>'' Entonces
									victoria <- Verdadero
								SiNo
									Si a=e Y e=i Y a<>'' Entonces
										victoria <- Verdadero
									SiNo
										Si c=e Y e=g Y c<>'' Entonces
											victoria <- Verdadero
										SiNo
											// No hay 3 en raya
											// Verificar empate
											Si  NO a='' Y  NO b='' Y  NO c='' Y  NO d='' Y  NO e='' Y  NO f='' Y  NO g='' Y  NO h='' Y  NO i='' Entonces
												final <- Verdadero
												mensajefinal <- 'Has Empatado'
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			// Decidir Ganador
			Si victoria=Verdadero Entonces
				final <- Verdadero
				Si turno=turnojugador Entonces
					mensajefinal <- 'Has Ganado'
				SiNo
					mensajefinal <- 'Has Perdido'
				FinSi
			FinSi
			victoria <- Falso
			// Cambiar turno
			Si turno=1 Entonces
				turno <- 2
			SiNo
				turno <- 1
			FinSi
			// Visualizar tablero
			Escribir a+' | '+b+' | '+c
			Escribir '-----------'
			Escribir d+' | '+e+' | '+f
			Escribir '-----------'
			Escribir g+' | '+h+' | '+i
		Hasta Que final=Verdadero
		Escribir mensajefinal
		//Jugar otra vez?
		auxsalida= falso
		Repetir
			Mostrar "Te gustaria volver a jugar? si o no"
			leer aux
			aux = Mayusculas(aux)
			segun aux
				"SI":
					FinalVerdadero = Falso
				"NO":
					FinalVerdadero = Verdadero
				De Otro Modo:
					Mostrar "Entrada Invalida. si o no"
			finsegun
		Hasta Que auxsalida = verdadero
		auxsalida = falso
		
	Hasta Que FinalVerdadero = verdadero	
FinAlgoritmo