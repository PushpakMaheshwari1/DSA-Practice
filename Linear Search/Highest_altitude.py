gain = [-4,-3,-2,-1,4,3,2]

output = 0
altitude = 0 
for i in gain:
    altitude = altitude + i
    output = max(altitude, output)
print(output)