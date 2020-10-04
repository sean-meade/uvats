u = (input("initial velocity: "))
v = (input("final velocity: "))
a = (input("acceleration: "))
t = (input("time: "))
s = (input("distance: "))

listOfInputs = [u, v, a, t, s]
convertedInputs = []

for i in listOfInputs:
    if i == '':
        convertedInputs.append(i)
    else:
        i = float(i)
        convertedInputs.append(i)

print(convertedInputs)

u = convertedInputs[0]
v = convertedInputs[1]
a = convertedInputs[2]
t = convertedInputs[3]
s = convertedInputs[4]

print(u, v, a, t, s)