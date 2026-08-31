funcion tablero <- actualizar_barcos_tablero (tablero, barcos)
	i = 1
	mientras barcos[i,1,3] = 1
		j = 1
		mientras j<= barcos[i,1,4]
			si barcos[i,j,5] = 1
				tablero[barcos[i,j,1],barcos[i,j,2]] = "X"
			FinSi
			j = j + 1
		FinMientras
		i = i + 1
	FinMientras
FinFuncion
funcion pos <- preguntar_coords
	n = 10
	m = 10
	mostrar "Ingrese coordenada x"
	auxsalida2 = Falso
	mientras auxsalida2 = falso Hacer
		leer c
		Si c>=1 Y c<=n
			auxsalida2 = Verdadero
		SiNo
			mostrar "Cooerdanada X invalida, esta debe estar entre 1 y 10"
		FinSi
	FinMientras
	mostrar "Ingrese coordenada y"
	auxsalida2 = Falso
	mientras auxsalida2 = falso hacer
		leer f
		si f>=1 Y f<=m Entonces
			auxsalida2 = verdadero
		SiNo
			mostrar "Coordenada Y invalida, esta debe estar entre 1 y 10"
		FinSi
	FinMientras
	Dimensionar pos[2]
	pos[1] = c
	pos[2] = f
FinFuncion
funcion xy <- extremo (c,f,largo,rotacion)
	si rotacion = "arriba"
		f = f - largo
	FinSi
	si rotacion = "abajo"
		f = f + largo
	FinSi
	si rotacion = "derecha"
		c = c + largo
	FinSi
	si rotacion = "izquierda"
		c = c - largo
	FinSi
	Dimensionar xy[2]
	xy[1] = c
	xy[2] = f
FinFuncion
funcion condicion <- detectar_choque(c,f,barcos)
	condicion = falso
	i = 1
	mientras barcos[i,1,3] = 1 Hacer
		j = 1
		mientras j <= barcos[i,1,4]
			si barcos[i,j,1] = c y barcos[i,j,2] = f
				condicion = Verdadero
			FinSi
			j = j + 1
		FinMientras
		i = i + 1
	FinMientras
FinFuncion
Funcion barcos <- crear_barco (c,f,largo,rotacion, barcos)
	i = 1
	mientras barcos[i,1,3] = 1
		i = i + 1
	FinMientras
	
	barcos[i,1,3] = 1
	barcos[i+1,1,3] = 0
	barcos[i,1,4] = largo
	j = 1
	mientras j <= largo
		Dimensionar xy[1]
		xy = extremo(c,f,j-1,rotacion)
		barcos[i,j,1] = xy[1]
		barcos[i,j,2] = xy[2]
		j = j + 1
	FinMientras
	
Fin Funcion

Función barcos <- atacar (c,f,tablero,barcos)
	Si tablero[c,f]='_' Entonces
		choque = falso
		i = 1
		mientras barcos[i,1,3] = 1 y choque es falso
			j = 1
			mientras j <= barcos[i,1,4] y choque es falso
				Dimensionar aux[1]
				si barcos[i,j,1] = c y barcos[i,j,2] = f
					choque = Verdadero
				FinSi
				j = j + 1
			FinMientras
			i = i + 1
		FinMientras
		si choque es verdadero
			mostrar "Le diste"
			barcos[i-1,j-1,5] = 1
		SiNo
			mostrar "No le has dado"
		finsi
	SiNo
		Escribir 'Posicion ya jugada'
	FinSi
FinFunción
Funcion condicion <- detectar_victoria(barcos)
	condicion = Verdadero
	i = 1
	mientras barcos[i,1,3] = 1 y condicion = Verdadero
		j = 1
		mientras j <= barcos[i,1,4] y condicion = Verdadero
			si barcos[i,j,5] = 0
				condicion = falso
			finsi
			j = j + 1
		finmientras
		i = i + 1
	FinMientras
FinFuncion
Función mostrar_matriz (matriz,m,n)
	// Mostrar matriz
	i <- 1
	Mientras i<=n Hacer
		j <- 1
		Mientras j<=m Hacer
			Escribir i, j, matriz[i,j]
			j <- j+1
		FinMientras
		i <- i+1
	FinMientras
FinFunción
Función matriz <- inicializar_matriz (m,n)
	Dimensionar matriz[n,m]
	// iniciar matriz
	i <- 1
	Mientras i<=n Hacer
		j <- 1
		Mientras j<=m Hacer
			matriz[i,j]<-'_'
			j <- j+1
		FinMientras
		i <- i+1
	FinMientras
FinFunción
Algoritmo batalla_naval
	n <- 10
	m <- 10
	dimensionar tablero_jugador[10,10]
	Dimensionar tablero_enemigo[10,10]
	tablero_jugador = inicializar_matriz(10,10)
	tablero_enemigo = inicializar_matriz(10,10)
	// El usuario elije si empieza primero o no
	Escribir 'Elija su turno. 1 para empezar primero y 2 para empezar segundo'
	auxsalida <- falso
	Mientras auxsalida=falso Hacer
		Leer turno
		Si turno=1 O turno=2 Entonces
			auxsalida <- Verdadero
		SiNo
			Escribir 'Entrada Invalida. Por favor escriba 1 o 2'
		FinSi
	FinMientras
	//Selecciona los barcos
	mostrar "Debes crear esconder tus barcos, dispones de 3 porta aviones ( ocupan 5 casillas), 3 destructores ( ocupan 3 casillas) y 3 Fragatas( ocupan 2 casillas)"
	portaviones = 3
	destructores = 3
	fragatas = 3
	Dimensionar tus_barcos[10,5,5]
	mientras portaviones > 0 o destructores > 0 o fragatas > 0 hacer
		mostrar "Elija un barco, 1 para porta aviones, 2 para destructor, 3 para fragata"
		auxsalida = Falso
		mientras auxsalida = falso Hacer
			leer x
			si x = "1"
				si portaviones > 0
					largo = 5
					auxsalida = Verdadero
					portaviones = portaviones - 1
					mostrar "Porta aviones seleccionado"
				SiNo
					mostrar "Porta aviones agotados, por favor elija otro barco"
				finsi
			SiNo
				si x = "2"
					si destructores > 0
						largo = 3
						auxsalida = Verdadero
						Mostrar "Destructor seleccionado"
					SiNo
						mostrar "destructores agotados, por favor elija otro barco"
					finsi
				SiNo
					si x = "3"
						si fragatas > 0
							largo = 2
							auxsalida = Verdadero
							mostrar "Fragata seleccionada"
						sino
							mostrar "fragatas agotadas, por favor elija otro barco"
						finsi
					Sino
						mostrar "Entrada no valida, elija 1, 2 o 3"
					FinSi
				FinSi
			FinSi
		FinMientras
		
		auxsalida = falso
		mientras auxsalida = falso Hacer
			Dimensionar pos[2]
			pos = preguntar_coords()
			c = pos[1]
			f = pos[2]
			mostrar "Ingrese rotacion: arriba, abajo, izquierda, derecha"
			auxsalida2 = Falso
			mientras auxsalida2 = falso Hacer
				leer rotacion
				si rotacion = "arriba" o rotacion = "abajo" o rotacion = "izquierda" o rotacion = "derecha"
					auxsalida2 = Verdadero
				SiNo
					mostrar "Entrada no valida no valida, la rotacion debe ser una de las siguientes: arriba, abajo, izquierda, derecha"
				FinSi
			FinMientras
			
			Dimensionar xy[2]
			xy[1] = 0
			xy[2] = 0
			xy = extremo(c,f, largo-1,rotacion) //RV
			ic = xy[1]
			if = xy[2]
			Si ic>0 Y ic<=n Y if>0 Y if<=m Entonces
				choque = falso
				i = 0
				mientras i <= largo-1 y choque es falso
					si rotacion = "arriba"
						choque = detectar_choque(c,f-i,tus_barcos)
					FinSi
					si rotacion = "abajo"
						choque = detectar_choque(c,f+i,tus_barcos)
					FinSi
					si rotacion = "derecha"
						choque = detectar_choque(c+i,f,tus_barcos)
					FinSi
					si rotacion = "izquierda"
						choque = detectar_choque(c-i,f,tus_barcos)
					FinSi
					i = i + 1
				FinMientras
				si choque es Falso
					tus_barcos = crear_barco(c,f,largo,rotacion,tus_barcos)
					auxsalida = Verdadero
					si x = "1"
						portaviones = portaviones - 1
					FinSi
					si x = "2"
						destructores = destructores - 1
					FinSi
					si x = "3"
						fragatas = fragatas - 1
					FinSi
				sino 
					mostrar "Colision con otro barco"
				FinSi
			sino
				mostrar "Parte del barco sobresale del mapa, pruebe con otra posicion/rotacion"
			FinSi
		FinMientras
	FinMientras
	//Le toca a la maquina seleccionar sus barcos
	Dimensionar barcos_enemigos[10,5,5]
	i = 1
	mientras i <= 3
		j = 1
		mientras j <= 3
			//barcos <- crear_barco (c,f,largo,rotacion, barcos)
			si i = 1
				k = 5
			FinSi
			si i = 2
				k = 3
			FinSi
			si i = 3
				k = 2
			FinSi
			barcos_enemigos = crear_barco((i-1)*3+j,1,k,"abajo",barcos_enemigos)
			j = j + 1
		FinMientras
		i = i + 1
	FinMientras
	// El juego empieza
	win = Falso
	mientras win = Falso
		//decide a quien le toca
		si turno = 1
			//juega el jugador 
			Mostrar "Turno del jugador"
			mostrar "En que coordenadas va a atacar? seleccion valida desde fila y columna 1 hasta la 10"
			Dimensionar pos[2]
			pos = preguntar_coords()
			barcos_enemigos = atacar(pos[1],pos[2],tablero_enemigo,barcos_enemigos)
			tablero_enemigo[pos[1],pos[2]] = "O"
			tablero_enemigo = actualizar_barcos_tablero(tablero_enemigo,barcos_enemigos)
			mostrar_matriz(tablero_enemigo,10,10)
		SiNo
			// juega la maquina
			mostrar "Turno de la maquina"
			repetida = Verdadero
			Mientras repetidda = Verdadero
				c = Aleatorio(1,10)
				f = Aleatorio(1,10)
				si tablero_jugador[c,f] = "_"
					repetida = Falso
				FinSi
			FinMientras
			//atacar
			tus_barcos = atacar(c,f,tablero_jugador, tus_barcos) //Función barcos <- atacar (c,f,tablero,barcos)
			tablero_jugador[c,f] = "O"
			tablero_jugador = actualizar_barcos_tablero(tablero_jugador,tus_barcos)
			mostrar_matriz(tablero_jugador,10,10)
		FinSi
		//detectar Victoria
		win1 = detectar_victoria(barcos_enemigos)
		win2 = detectar_victoria(tus_barcos)
		si win1 = Verdadero
			mostrar "has ganado"
			win = Verdadero
		SiNo
			si win2 = Verdadero
				mostrar "has perdido"
				win = Verdadero
			FinSi
		FinSi
		// cambio de turno
		si turno = 1
			turno = 2
		SiNo
			turno = 1
		FinSi
	FinMientras
FinAlgoritmo
