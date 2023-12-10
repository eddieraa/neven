value="1e24"
v=value.split("e")

if int(v[1])>26:
    result = str(round(float(v[0])*10**(int(v[1])-27),3))+" Octillions"
elif int(v[1])>23:
    result = str(round(float(v[0])*10**(int(v[1])-24),3))+" Septillions"
elif int(v[1])>20:
    result = str(round(float(v[0])*10**(int(v[1])-21),3))+" Sextillions"
elif int(v[1])>17:
    result = str(round(float(v[0])*10**(int(v[1])-18),3))+" Quintillions"
elif int(v[1])>14:
    result = str(round(float(v[0])*10**(int(v[1])-15),3))+" Quadrillions"
elif int(v[1])>11:
    result = str(round(float(v[0])*10**(int(v[1])-12),3))+" Trillions"
elif int(v[1])>8:
    result = str(round(float(v[0])*10**(int(v[1])-9),3))+" Billions"
elif int(v[1])>5:
    result = str(round(float(v[0])*10**(int(v[1])-6),3))+" Millions"
else:
    result = str(eval(value))
print(result)