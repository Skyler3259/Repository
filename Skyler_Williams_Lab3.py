speedlimit = int(input("What is the speed limit?  "))

carspeed = int(input("What is your speed?  "))

x = (carspeed - speedlimit)//5

print(x) 
print("Demerit points")

if x >= 12: print("License suspended.")