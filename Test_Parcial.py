import math
import random
import simpy 

cont1 = 0
cont2 = 0
cont3 = 0

def simulacion(env):
    global cont1
    global cont2
    global cont3
    
    dias = 0
    R = random.random()
 
    while True:
        dias += 1
        print("Simulacion de trafico dia {0}".format(dias),)
        print("Horario por la mañana ".format(str(env.now)))
        d_mañana = 5
        R = (random.randrange(1000))
        cont1 += R
        print(cont1, "autos")
        yield env.timeout(d_mañana)
        
        print("Horario por la tarde ".format(str(env.now)))
        d_tarde = 3
        R = (random.randrange(1000))
        cont2 += R
        print(cont2, "autos")
        yield env.timeout(d_tarde)
        
        print("Horario por la noche ".format(str(env.now)))
        d_noche = 4
        R = (random.randrange(1000))
        cont3 += R
        print(cont3, "autos")
        yield env.timeout(d_noche)
       


if __name__== '__main__':
    env = simpy.Environment()
    env.process(simulacion(env))
    env.run(until= 372)
    total = math.floor(cont1 + cont2 + cont3)
    print("El trafico total por la mañana: ",cont1, " autos" )
    print("El trafico total por la tarde: ",cont2, " autos")
    print("El trafico total por la noche: ",cont3, " autos")
    print("El total de trafico de la simulacion es: ",total, "autos")
    print("Promedio del trafico entre cada horario es: ",math.floor(total/3))
    print("En el dia 15, el trafico de la mañana es de: ",math.floor(cont1*15/31), " autos")
    

