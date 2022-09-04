from tabulate import tabulate


class Prestamo:
    file = "C:/Users/anaso/Documents/DABM/LAB2/database/prestamo.csv"
    def __init__(self,nombre,carnet,equipo,FechaP,FechaE):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.FechaP = FechaP
        self.FechaE = FechaE
    
    def save(self):
        f = open(self.file,'a')
        linea = ";".join([self.nombre,self.carnet,self.equipo,self.FechaP,self.FechaE])
        f.write(linea+"\n")
        f.close()
    

def crearPrestamo():
    print('Registrar nuevo prestamo')
    nombre = input("Nombre: ")
    carnet = input("Carnet: ")
    equipo = input("equipo: ")
    FechaP = input("Fecha del prestamo (yyyy-mm-dd): ")
    FechaE = input("Fecha de entrega (yyyy-mm-dd): ")

    p = Prestamo(nombre,carnet,equipo,FechaP,FechaE)

    return p

def registroEntrega():
    ListaPrestamos = getAllPrestamos()
    carnet = input("Carnet del estudiante que solicitó el prestamo: ")
    equipo = input("Equipo: ")
    #print(ListaPrestamos)
    for p in ListaPrestamos:
        #print(p)
        if equipo in p:
            if carnet in p:
                ListaPrestamos.remove(p)
    #print(ListaPrestamos)
    saveAllPrestamos(ListaPrestamos)

def saveAllPrestamos(equipo):
    a = open("C:/Users/anaso/Documents/DABM/LAB2/database/prestamo.csv","w")
    for p in equipo:
        a.write(p)
    a.close()
            
def getAllPrestamos():
    a = open("C:/Users/anaso/Documents/DABM/LAB2/database/prestamo.csv","r")
    datos = a.readlines()
    return datos

def verPrestamos():
    ListaPrestamos = getAllPrestamos()
    carnet = input("Ingrese su número de carnet: ")
    header = ['Nombre','Carnet','Equipo','Fecha del prestamo','Fecha de devolución']
    filas = []
    #print(ListaPrestamos)
    for p in ListaPrestamos:
        #print(p)
        if carnet in p:
            #print(p)
            datos = p.split(";")
            filas.append(datos)
            #print(datos)
    print(tabulate(filas, header, tablefmt="grid"))
