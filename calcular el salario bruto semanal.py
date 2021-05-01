"""
La Asociación Gusto por la Vida, desea calcular el salario bruto semanal
de un empleado (sin deducciones) y su respectivo salario neto semanal 
(con deducciones). 
Para cada empleado se lee la cantidad de horas por trabajadas. 
Un empleado puede trabajar en jornada ordinaria hasta 48 horas por semana, y un máximo de 24 horas extras.
Leer el nombre del empleado, la cantidad de horas laboradas y el salario por hora. 
Determinar el monto de salario ordinario, salario extra y el total de salario bruto.
Además, mostrar el monto de deducción de la CCSS (correspondiente al 10.66%) y 
finalmente el salario neto luego de aplicar la deducción.
"""


nombre = input("Nombre del empleado: ")
horas = int(input("Horas Laboradas = "))
salHora = float(input("Salario por hora= ")) 

if horas <=48:
    salOrd = horas * salHora
    salExt = 0
else:
    salOrd = 48 * salHora
    horasExt = horas - 48
    if horasExt <= 24:
        salExt = horasExt * salHora * 1.5
    else:
        salExt = 24 * salHora * 1.5

salBruto = salOrd + salExt
deduc = salBruto * 0.1066
salNeto = salBruto - deduc

print("Salario ordinario = " , salOrd)
print("Salario Extra = " , salExt)
print("Salario Bruto = " , salBruto)
print("Deducción de la CCSS = " , deduc)
print("Salario neto = " , salNeto)

