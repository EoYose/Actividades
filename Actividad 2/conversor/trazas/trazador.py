#20-04-2026
import pandas as pd
class Archivo:
	#Representa un archivo de excel, usa clases Hoja
	def __init__(self,nombre:str,*hojas):
		self.nombre = nombre
		self.hojas = hojas
	def crear_excel(self):
		with pd.ExcelWriter(f"{self.nombre}.xlsx") as writer:
			for i in self.hojas:
				i.get_dataframe().to_excel(writer,sheet_name=i.name,index=False)
class Hoja:
	def __init__(self,nombre:str,diccionario:dict={}):
		self.diccionario = diccionario
		self.name = nombre
	def modify(self,**kwargs):
		for key, value in kwargs.items():
			self.diccionario[key] = value
	def add(self, **kwargs):
	    for key in self.diccionario:
	        if key in kwargs:
	            self.diccionario[key].append(kwargs[key])
	        else:
	            self.diccionario[key].append("")  # o None
	def get_dataframe(self):
		return pd.DataFrame(self.diccionario) 
class Counter:
	def __init__(self,count:int=0,texto:str=""):
		self.count = count
		self.texto = texto
		self.inicio = True
	def get(self):
		self.count +=1
		return self.count
	def get_str(self):
		self.count += 1
		if self.inicio:
			self.inicio = False
			self.count-=1
			return "Inicio"
		return self.texto + str(self.count)
class GestorTrazas:
	def __init__(self, nombre_archivo):
		self.nombre_archivo = nombre_archivo
		self.hojas = []

	def ejecutar(self, nombre_hoja, funcion, args, columnas):
		conteo = Counter(texto="Fase ")
		hoja = Hoja(nombre_hoja, {"fase": [], **{col: [] for col in columnas}})

		def trace(**kwargs):
			hoja.add(fase=conteo.get_str(), **kwargs)

		# estado inicial opcional (útil para claridad)
		#hoja.add(fase="Inicio", **{col: "" for col in columnas})

		funcion(*args, trace=trace)

		self.hojas.append(hoja)

	def guardar(self):
		archivo = Archivo(self.nombre_archivo, *self.hojas)
		archivo.crear_excel()

def bin_to_dec(binario):
	decimal = 0
	base = 1
	hoja.add(fase="Datos Iniciales",binario=binario,decimal=decimal,base=base,digito="")
	while not binario==0:
		digito = binario%10
		if digito == 1:
			binario = binario - 1
		decimal = decimal + digito*base
		binario = binario//10
		base = base*2
		hoja.add(fase=conteo.get_str(),binario=binario,decimal=decimal,base=base,digito=digito)
	return decimal
if __name__ == "__main__":
	conteo=Counter(texto="Fase ")
	hoja = Hoja("Prueba1",{"fase":[],"binario":[],"decimal":[],"base":[],"digito":[]})
	bin_to_dec(1010)
	a = Archivo("Test",hoja)
	a.crear_excel()