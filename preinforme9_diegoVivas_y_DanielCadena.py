x = input(("inserte su numero: "))

def fninverso (sDato):
    rta = ""
    end=len(sDato) - 1
    while (end >=0):
        rta = rta + sDato[end]
        end = end - 1
    return rta

print ("el numero invertido es: ", fninverso(x))