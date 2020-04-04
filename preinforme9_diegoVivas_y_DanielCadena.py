x1 = float(input('inserte el valor de la nota 1: '))
x2 = float(input('inserte el valor de la nota 2: '))
x3 = float(input('inserte el valor de la nota 3: '))
x4 = float(input('inserte el valor de la nota 4: '))
x5 = float(input('inserte el valor de la nota 5: '))

n1= x1*0.15
n2= x2*0.2
n3= x3*0.15
n4= x4*0.3
n5= x5*0.2
avg = n1 + n2 + n3 + n4 + n5

if  avg <2 :
    print ('no puede habilitar', avg)
elif avg < 3 :
    print ('reprobó', avg)
elif avg>=3.0 and avg <= 4.5:
    print('aprobó', avg)
elif avg > 4.5 :
    print ('felicitaciones', avg)
pass