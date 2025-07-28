def calcular_promedio_de_examenes():
    calificaciones=[]#Aqui se guardan las califaciones del examen
    try:
        print("Ingresa la cantidad examenes durante el curso:")
        examenes=int(input())
        if examenes <0 or examenes == 0:
            print("No se permite valores menores a 0 ")
        print("Ingresa la calificacion de cada examen")
        
    except ValueError:
        print("Ingresa un numero entero!")
        return

    for i in range(examenes):
        calificacion=int(input(f"Ingresa la calificacion del examen {i+1}:\n"))
        calificaciones.append(calificacion)
    print("Las calificaciones ingresadas son: ", calificaciones)
    input("Presione enter para continuar")

    #Calcular el promedio
    sumar=sum(calificaciones)
    promedio=sumar/len(calificaciones)
    print("El promedio de los examenes es: ",promedio)
    print("="*30)


def calcular_promedio_de_tareas():
    calificaciones_tareas=[]
    try:
        tareas=int(input("Ingresa la cantidad de tareas:\n"))
        if tareas<0 or tareas == 0: 
            print("No se permiten valores menores a 0")
    
    except ValueError:
        print("Ingresa un numero entero!")
        
    for i in range(tareas):
        tarea=int(input(f"Ingresa la calificacion de la tarea {i+1}:\n"))
        calificaciones_tareas.append(tarea)
    print("Las calificaciones de las tareas son:\n", calificaciones_tareas)
    input("Presiona enter para continuar")

    sumar=sum(calificaciones_tareas)
    promedio=sumar/len(calificaciones_tareas)
    print("El promedio de las tareas es: ",promedio)
    print("="*30)

def examenes_y_tareas():
    while True:
        calificaciones=[]
        porcentajes=[]
        calificaciones_tareas=[]
        porcentajes_tareas=[]
        puntos_totales=0 #Examenes
        puntos_totales_tareas=0 #Tareas
        
        examenes=int(input("Ingresa la cantidad de examenes:\n"))
        tareas=int(input("Ingresa la cantidad de tarea:\n"))
        
        if examenes <=0:
                print("No se permiten valores negativos o nulos")
                
        else:
            for i in range(examenes):
                nota=int(input(f"Ingresa la calificacion obtenida en el examen {i+1}:\n"))
                porcentaje=int(input(f"Ingresa el valor del examen {i+1}:\n"))
                calificaciones.append(nota)
                porcentajes.append(porcentaje)
                
            for x in range(tareas):
                notas=int(input(f"Ingresa la calificacion otenida en la tarea #{x+1}:\n"))
                valor=int(input(f"Ingresa el valor de la tarea #{x+1}:\n"))
                calificaciones_tareas.append(notas)
                porcentajes_tareas.append(valor)
                
                
            print("Las calificaciones de los examenes son:\n",calificaciones)
            print("Los porcentajes del valor de los examenes son:\n",porcentajes)
            print("Las calificaciones de las tareas son:\n",calificaciones_tareas)
            print("Los valores de las tareas son: \n",porcentajes_tareas)
            input("Presiona enter para continuar")


            #Examenes
            for x, (calificacion, porcentaje) in enumerate(zip(calificaciones, porcentajes)):
                puntos=(calificacion/100)*porcentaje
                puntos_totales += puntos
                print(f"Examen {x+1}; Calificacion: {calificacion}, Valor: {porcentaje}, Puntos obtenidos: {puntos:.2f}")
                
            print("="*30)

                #Tareas
            for z, (nota, porcentajes_tareas) in enumerate(zip(calificaciones_tareas, porcentajes_tareas)):
                puntos_tareas=(nota/100)*porcentajes_tareas
                puntos_totales_tareas+=puntos_tareas
                print(f"Tarea {z+1}; Calificacion: {nota}, valor: {porcentajes_tareas}, puntos obtenidos: {puntos_tareas:.2f}")

            print("="*30)
            print("La suma total de puntos de examenes es de: ", puntos_totales)
            print("La suma total de puntos de tareas es de: ", puntos_totales_tareas)   
            print("="*30)

        break

def menu_principal():
    while True:
        print("Bienvenido al sistema de promedios y evaluaciones!\nIngresa una de las opciones a continuacion\n1)Promediar resultados de examenes\n2)Promediar resultados de tareas\n3)Calcular evaluacion\n4)Salir")
        try:
            opcion=int(input())
            if opcion == 1:
                calcular_promedio_de_examenes()
            elif opcion == 2:
                calcular_promedio_de_tareas()
            elif opcion == 3:
                examenes_y_tareas()
            elif opcion == 4:
                break
        except ValueError:
            print("Ingresa un numero entero!")
            continue


menu_principal()