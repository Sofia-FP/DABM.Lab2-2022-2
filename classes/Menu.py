
class menu:
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio
    
    def ver(self):
        print("Bienvenido al sistema".center(20,"*"))
        print("Laboartorio: "+self.laboratorio)
        print("1. Técnicos")
        print("2. Estudiantes")
        op = input(">>>")

        return op

class MenuTecnicos:
    def ver(self):
        print("Menú Técnicos de Laboratorio".center(20,"*"))
        print("1. Registrar equipos")
        print("2. Registrar prestamo")
        print("3. Registrar matenimiento")
        print("4. Registrar entrega")
        op = input(">>>")

        return op

class MenuEstudiantes:
    def ver(self):
        print("Menú Estudiantes".center(20,"*"))
        print("1. Ver prestamos")
        print("2. consultarEquipo")
        op = input(">>>")

        return op

if __name__=='__main__':
    m = menu("xxx")
    m.ver()