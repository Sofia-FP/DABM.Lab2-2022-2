from tabulate import tabulate

class Equipo:
    file = "C:/Users/anaso/Documents/DABM/LAB2/database/equipo.csv"
    def __init__(self,nombre,referencia,proveedor,cicloM,cantidad,FechaUM=""):
        self.nombre = nombre
        self.referencia = referencia
        self.proveedor = proveedor
        self.cicloM = cicloM
        self.FechaUM = FechaUM
        self.cantidad = cantidad

    def verDatos(self):
        header = ["NOMBRE","REFERENCIA","PROVEEDOR","CICLO","CANTIDAD","FECHAUM"]
        datos = [[self.nombre,self.referencia,self.proveedor,self.cicloM,self.cantidad,self.FechaUM]]
        print(tabulate(datos, header, tablefmt="grid"))

    def save(self):
        f = open(self.file,'a')
        linea = ";".join([self.nombre,self.referencia,self.proveedor,self.cicloM,self.cantidad,self.FechaUM])
        f.write(linea+"\n")
        f.close()

    def consulta(self,Nombre):
        pass

def crearEquipo():
    print('Registrar nuevo equipo')
    nombre = input("Nombre: ")
    referencia = input("Referencia: ")
    proveedor = input("Proveedor: ")
    cicloM = input("Ciclo de mantenimiento (días): ")
    cantidad = input("Cantidad de equipos: ")
    FechaUM = input("Última fecha de mantenimiento (yyyy-mm-dd): ")

    e = Equipo(nombre,referencia,proveedor,cicloM,cantidad,FechaUM)

    return e

def consultaEquipo():
    print('Consulta de equipos')
    nombre = input("Nombre del equipo: ")

def registroMantenimiento():
    ListaEquipos = getAllEquipos()
    equipo = input("Equipo: ")
    FechaUM = input("Fecha de último mantenimiento (yyyy-mm-dd): ")
    pos = 0
    for e in ListaEquipos:
        if equipo in e:
            datosEquipo = e.split(";")
            datosEquipo[5] = FechaUM + "\n"
            ListaEquipos[pos] = ";".join(datosEquipo)
        pos+=1
    saveAllEquipos(ListaEquipos)

def saveAllEquipos(equipo):
    a = open("C:/Users/anaso/Documents/DABM/LAB2/database/equipo.csv","w")
    for e in equipo:
        a.write(e)
    a.close()

def getAllEquipos():
    a = open("C:/Users/anaso/Documents/DABM/LAB2/database/equipo.csv","r")
    datos = a.readlines()
    return datos

def consultarEquipo():
    pass
