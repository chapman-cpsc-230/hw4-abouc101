def H(x):
    if x < 0:
        return 0
    if x >= 0:
        return 1

def test_H():
    if H(-10) != 0:
        print "Error1"
    elif H(-10**-15) != 0:
        print "Error2"
    elif H(0) != 1:
        print "Error3"
    elif H(10**-15) != 1:
        print "Error4"
    elif H(10) != 1:
        print "Error5"
    else:
        print "Correct"

test_H()

name = input('')
