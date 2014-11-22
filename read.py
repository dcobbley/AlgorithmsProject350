__author__ = 'Sam'
f = open('USA.txt')
lines = f.readlines()
#content = f.readlines()
#print (lines)
current = 0
while current < len(lines):
     #print lines[current]
     current += 1
line1 = lines[1].split("\\s")
line1 =" ".join(line1[0].split())
line1 =  line1.split(" ");
print line1[2]
f.close()
