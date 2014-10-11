database = open("WeaponSubTypes DB", "r")
newpycode = open("WeaponSubTypeIndex", "w")
tempString = ""

newpycode.write("dict = {")
for i in range(1,29):
	tempString = database.readline().rstrip()
	newpycode.write(str(i))
	newpycode.write(":")
	newpycode.write("\"")
	newpycode.write(tempString)
	newpycode.write("\"")
	if i != 28:
		newpycode.write(", ")
newpycode.write("}")