from trazador import *

entrada_trazas = {
"dec_bin":[(65,),(9,),(24,)],
"dec_hex":[(65,),(5000,),(24,)],
"dec_oct":[(65,),(500,),(24,)],
"hex_dec":[("A2",),("C9",),("53",)],
"oct_dec":[(71,),(213,),(21,)],
"bin_dec":[(10010,),(1001,),(10000010,)]
}

db=GestorTrazas("trazas_dec_bin")
def dec_bin(decimal,trace=None):
	binario = 0
	vueltas = 0
	digito = 0
	if trace:
		trace(decimal=decimal, binario=binario,vueltas=vueltas,digito=digito)
	while not decimal <=1:
		digito = decimal%2
		if digito == 1:
			decimal-=1
		binario += digito*10**vueltas
		decimal = decimal//2
		vueltas += 1
		if trace:
			trace(decimal=decimal,binario=binario,vueltas=vueltas,digito=digito)
	binario += decimal*10**vueltas
	trace(decimal="",binario=binario,vueltas="",digito="")
	return str(binario)
for i in range(3):
	db.ejecutar(f"Ejemplo {i}",dec_bin,entrada_trazas["dec_bin"][i],["decimal","binario","vueltas","digito"])
db.guardar()
dh=GestorTrazas("trazas_dec_hex")
def dec_hex(decimal,trace=None):
	hexadecimal = ""
	hex_list = "0123456789ABCDEF"
	if trace:
		trace(hexadecimal=hexadecimal,digito="",decimal=decimal)
	while not decimal < 16:
		digito = decimal%16
		decimal -=digito
		hexadecimal = hexadecimal + hex_list[digito]
		decimal = decimal//16
		if trace:
			trace(hexadecimal=hexadecimal,digito=digito,decimal=decimal)
	hexadecimal = hex_list[decimal] + hexadecimal
	if trace:
		trace(hexadecimal=hexadecimal,digito="",decimal="")
	return hexadecimal
for i in range(3):
	dh.ejecutar(f"Ejemplo {i}",dec_hex,entrada_trazas["dec_hex"][i],["decimal","hexadecimal","digito"])
dh.guardar()
do=GestorTrazas("trazas_dec_oct")
def dec_oct(decimal,trace=None):
	octal = 0
	base = 1
	if trace:
		trace(decimal=decimal,octal=octal,base=base,digito="")
	while not decimal < 8:
		digito = decimal%8
		decimal -=digito
		octal += digito*base
		decimal /=8
		base*=10
		if trace:
			trace(decimal=decimal,octal=octal,base=base,digito=digito)
	octal+=round(decimal*base)
	if trace:
			trace(octal=octal)
	return octal
for i in range(3):
	do.ejecutar(f"Ejemplo {i}",dec_oct,entrada_trazas["dec_oct"][i],["decimal","octal","base","digito"])
do.guardar()
hc=GestorTrazas("trazas_hex_dec")
def hex_dec(hexadecimal,trace=None):
	hexadecimal = hexadecimal.replace(" ","")
	hex_chars = "0123456789ABCDEF"
	decimal = 0
	base = 1
	if trace:
		trace(hexadecimal=hexadecimal,decimal=decimal,base=base,aux="",aux1="")
	for aux in hexadecimal[::-1]:
		aux1 = hex_chars.index(str(aux.upper()))
		decimal += aux1*base
		base*=16
		if trace:
			trace(aux=aux,aux1=aux1,decimal=decimal,base=base,hexadecimal=hexadecimal)
	return decimal
for i in range(3):
	hc.ejecutar(f"Ejemplo {i}",hex_dec,entrada_trazas["hex_dec"][i],["hexadecimal","decimal","base","aux","aux1"])
hc.guardar()
oc=GestorTrazas("trazas_oct_dec")
def oct_dec(octal,trace=None):
	octal = int(octal)
	decimal = 0
	base = 1
	if trace:
		trace(octal=octal,decimal=decimal,base=base,digito="")
	while not octal<8:
		digito = octal%10
		octal -= digito
		decimal = decimal + digito*base
		octal = octal//10
		base = base*8
		if trace:
			trace(digito=digito,octal=octal,base=base,decimal=decimal)
	decimal = decimal + octal*base
	if trace:
		trace(decimal=decimal)
	return decimal
for i in range(3):
	oc.ejecutar(f"Ejemplo {i}",oct_dec,entrada_trazas["oct_dec"][i],["octal","decimal","base","digito"])
oc.guardar()
bd=GestorTrazas("trazas_bin_dec")
def bin_dec(binario,trace=None):
	binario=int(binario)
	decimal = 0
	base = 1
	if trace:
		trace(binario=binario,decimal=decimal,base=base,digito="")
	while not binario==0:
		digito = binario%10
		if digito == 1:
			binario = binario - 1
		decimal = decimal + digito*base
		binario = binario//10
		base = base*2
		if trace:
			trace(digito=digito,binario=binario,base=base,decimal=decimal)
	return decimal
for i in range(3):
	bd.ejecutar(f"Ejemplo {i}",bin_dec,entrada_trazas["bin_dec"][i],["binario","decimal","base","digito"])
bd.guardar()