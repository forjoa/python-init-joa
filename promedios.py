def avg(lista: list):
    return sum(lista)/len(lista)

estudiantes = {
    "Ana": [8, 9, 10], 
    "Luis": [7, 6, 8], 
    "Carlos": [9, 10, 10]
}

promedio_ana=avg(estudiantes['Ana'])
print(promedio_ana)

promedio_luis=avg(estudiantes["Luis"])
print(promedio_luis)

promedio_carlos=avg(estudiantes["Carlos"])
print(promedio_carlos)

promedio_clase=avg([promedio_ana, promedio_luis, promedio_carlos])
print (promedio_clase)









