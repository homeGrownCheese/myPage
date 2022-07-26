fname = input("Enter File: ")
hand = open(fname)
f = open("Nascar_standings_new.txt", "a")
f.write("<table>" + "\n")
f.write("<tr><th>Name</th><th>Points</th></tr>" + "\n")

for line in hand:
    line = line.rstrip()
    line = line.split(",")
    name = line[1].split()
    name = name[0]
    total_points = line[9]
    line = "<tr><td>" + name + "</td><td>" + total_points + "</td></tr>" + "\n"
    f.write(line)

f.write("</table>")
