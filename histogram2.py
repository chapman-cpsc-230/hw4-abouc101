hs = [4, 9, 13, 5]
print """
 n  | Data
---+------------------
"""
def bar(n):
    st = ''

    for i in range(n):
        st += '*'
    return st
print hs
for i in range(len(hs)):
    print bar(hs[i])
name = raw_input("")
#could not figure this out
