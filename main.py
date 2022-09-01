
from classes.Menu import *
from classes.Equipo import *
from classes.Prestamo import *

def main():
    Menu = menu("Escuela Colombiana de Ingeniería")
    op = Menu.ver()
    if op == "1":
        Menu2 = MenuTecnicos()
        op2 = Menu2.ver()
        if op2 == "1":
            e = crearEquipo()
            e.verDatos()
            e.save()
        elif op2 == "2":
            p = crearPrestamo()
            p.save()
        elif op2 == "3":
            registroMantenimiento()
        elif op2 == "4":
            registroEntrega()
        else:
            print('Opción inválida')
            main()
    elif op=='2':
        Menu2 = MenuEstudiantes()
        op2 = Menu2.ver()
        if op2 == '1':
            verPrestamos()
        elif op2 == '2':
            consultarEquipo()
        

if __name__=='__main__':
   
    main()