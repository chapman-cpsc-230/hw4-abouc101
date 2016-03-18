from math import pi
from math import sin
def H_eps(x,eps=0.01):
    if x < - eps:
        result = 0
    elif x <= eps:
        XoverEPS= (x/eps)
        result = 0.5*(1+(XoverEPS)+(sin(pi*(XoverEPS)))/pi)
    else:
        result = 1
    return result

def Test_H_eps():
    if H_eps(-0.02)!= 0:
        print "Error1"
    elif H_eps(-0.01) != 0.5 * (1 + (-0.01/0.01) + (sin(pi *(-0.01/0.01)))/pi):
        print "Error2"
    elif H_eps(0) != 0.5 * (1 + (0/0.01) + (sin(pi *(0/0.01)))/pi):
        print "Error3"
    elif H_eps(0.02) != 1:
        print "Error4"
    else:
        print "Correct"

Test_H_eps()

name = raw_input('')
