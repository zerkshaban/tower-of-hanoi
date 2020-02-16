def tower(n, fr, spare, to):
    if n == 1 :
        print("move " + str(fr)+" to "+str(to))
    else:
        tower(n-1, fr, spare, to)
        tower(1, fr, to, spare)
        tower(n-1, spare, to, fr)


tower(5,'f','t','s')