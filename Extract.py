with open("a.txt") as file:
	lines = file.readlines()

destination = open("dest.txt", "w")
for line in lines:
	destination.write("%s\n" % line.split(" ")[0])