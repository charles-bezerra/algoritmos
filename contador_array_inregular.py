l = [1,1, [1, [1,1,1,[1,1,1,1]],[1,1,1,1]], [1,1,1]]

def conta(l, c=0):
    contador=c
    for e in l:
        if type(e) == list:
            contador=conta(e,contador)
        else:
            contador+=e
    return contador