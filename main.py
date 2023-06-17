from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("------herencia alumno-----")
    al1 = Alumno("Jose", 19, "23476543", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("----------herencia profesor-------------")
    profe1= Profesor("Jesus", 30 +16, 2345, "Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("-------herencia ayudante profe-----")
    ayudante = AyudanteProfesor("Adrian", 20, "12345", "ICO", 43682, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    


main()

