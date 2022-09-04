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
            print(" ")
            main()
        elif op2 == "2":
            p = crearPrestamo()
            p.save()
            print(" ")
            main()
        elif op2 == "3":
            registroMantenimiento()
            print(" ")
            main()
        elif op2 == "4":
            registroEntrega()
            print(" ")
            main()
        else:
            print('Opción inválida')
            print(" ")
            main()
    elif op == '2':
        Menu2 = MenuEstudiantes()
        op2 = Menu2.ver()
        if op2 == '1':
            verPrestamos()
            print(" ")
            main()
        elif op2 == '2':
            consultarEquipo()
            print(" ")
            main()
        else:
            print('Opción inválida')
            print(" ")
            main()
    elif op == '3':
        quit()
        

if __name__=='__main__':
   
    main()