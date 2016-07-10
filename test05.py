def fact(i):
    if i==1 or i==0:
        return 1
    return i*fact(i-1)
print fact(5)
