import os
def menu():
    print('Seleccione una opciòn:')
    print('1) crear archivo')
    print('2) agregar datos al archivo')
    print('3) listar contenido del archivo')
    print('4) eliminar contenido del archivo')
    print('5) borrar archivo')
    print('6) copiar archivo')
    print('7) salir')
def crear_archivo(direccion):
    f = open(direccion,'w')
    f.close()
def agregar_datos(direccion):
    f = open(direccion,'a')
    nombre = input('nombre: ')
    ap_pat = input('apellido paterno: ')
    ap_mat = input('apellido materno: ')
    f.write(nombre+' '+ap_pat+' '+ap_mat+'\n')
    f.close()
def mostrar_archivo(direccion):
    f = open(direccion,'r')
    L=f.readline()
    while L!='':
        print(L)
        L=f.readline()
    f.close()
def eliminar_archivo(direccion):
    if os.path.exist(direccion):
        os.remove(direccion)
    else:
        print('no encontro el archivo')
def leer_opcion():
    while True:
        opcion = input('ingrese numero: ')
        if opcion.isdigit():
            opcion = int(opcion)
            if  (1 <= opcion <= 7):
                break
            else:
                print('valor fuera de rango')
        else:
            print('opcion no valida')
    return opcion
def inicio():
    direccion = 'Alumnos.txt'
    opcion = 0
    while True:
        menu()
        op = leer_opcion()
        if op==1:
            crear_archivo(direccion)
        elif op == 2:
            agregar_datos(direccion)
        elif op == 3:
            mostrar_archivo(direccion)
        elif op == 5:
            ruta = 'alumnos.txt'
            eliminar_archivo(ruta)
        else:
            break
inicio()