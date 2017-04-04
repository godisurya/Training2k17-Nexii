a = input("Total number of people: ")
b = input("Total number of busses: ")
c = input("Number of seats for bus: ")
d = (b*c)
e = (d-a)
f = (a-d)

if a == d or a <= d:
    print "There are sufficient busses and the remaining seats are %d" %(e)

else:
    print "There are no sufficient busses and the seats required are %d" %(f)
