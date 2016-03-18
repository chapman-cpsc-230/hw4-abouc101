hs = [4, 9, 13, 5]
def bar(n):
    st = ''
    for i in range(n):
        st += '*'
    return st

for i in range(len(hs)):
    print bar(hs[i])
name = raw_input("")
