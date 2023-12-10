val=[1.5,2.5,4,10,25,100,1000]
valnew=[1.5,2.5,4,10,25,100,1000]
xp=[5123,5200,5300,5711,5400,5111,5000]
for i in range(7):
    xi=150
    valnew[i]=val[i]
    while xp[i]>xi:
        valnew[i]=round(valnew[i]*1.5,1)
        xi*=3