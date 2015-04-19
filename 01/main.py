for i in range(1,10):
    s=""
    for j in range(1,10):
        if(i<j):
            continue
        else:
            s+=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
    print(s)
print("\n")
for i in range(1,10):
    s=""
    for j in range(1,10):
        if(j<i):
            print(end="       ")
            continue
        else:
            s+=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
    print(s)
print("\n")
for i in range(1,10):
    s=""
    for j in range(1,10):
        if(j<i):
            continue
        else:
            s+=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
    print(s)
