import numpy as np
import matplotlib.pyplot as plt

def EulerO1(fonction,init,interval,point_number):
    #fonction est la fonction qui renvoie le float tq df/dt = f(x,t), elle correspond donc à l'équation à intégrer de condition initiale init
    #interval la liste correspondant à l'interval d'integration
    start,end=interval
    step = abs((start-end)/point_number)
    curr_f = init
    res = [init]
    for i in range(1,point_number+1):
        curr_t = start + i*step
        curr_f = curr_f + step*fonction(curr_f,curr_t)
        res += [curr_f]
    return res