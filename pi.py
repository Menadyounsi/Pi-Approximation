import math

piover4 = 1.0
realpi = math.pi
realpiby4 = 0.25*realpi
denominator = 3.0
x = True
dp = 1
pifinal = piover4

print "This app allows you to calculate Pi to a given accuracy using the Leibniz formula for Pi"
epsilon = float(raw_input("To what accuracy would you like to calulate Pi? > "))

epsilon_by_4 = 0.25*(epsilon)

while (abs(realpiby4 - piover4) >= epsilon_by_4):
    if dp % 2 == 0:
        piover4 = piover4 + (1.0/denominator)
        denominator = denominator + 2.0
        dp += 1

    else:
        piover4 = piover4 - (1.0/denominator)
        denominator = denominator + 2.0
        dp += 1.0

print "\nValue of mathpi:"
print "%.10f" % round(realpi,10)
print "\nApproximation of Pi:"
print "%.10f" % round((4*piover4),10)
print "\nIterations:"
print dp
