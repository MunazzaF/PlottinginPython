
import numpy
import matplotlib.pyplot

#A is the amplitude in volts.
# ω the angular frequency
# Lambda is the wave length
#c is the speed of light
# f is the fundamental frequency
#0=<φ=<2(pi) radians is the initial phase

def Dxt( A, k, omega, phi, fixed, param, data):
    if fixed == 0:
        data = data*k + numpy.full(data.shape, omega * param - phi)  
    elif fixed == 1:
       data = -omega * data + numpy.full(data.shape, k * param + phi)
    else:
        pass
    return A * numpy.sin(data)

z = (10 ** 8)*3 

f1 = 5
f2 = 3

A1 = 5
A2 = 3

phisquare1 = 0
phisquare2 = numpy.pi / 3

fixedx1 = 5
fixedt1 = 10

lambda1 = z / f1
lambda2 = z / f2

omega1 = 2 * numpy.pi * f1
omega2 = 2 * numpy.pi * f2

k1 = 1
k2 = (2 * numpy.pi) / lambda2


fixedx2 = 7
fixedt2 = 18

data = numpy.linspace(0, 10, 1000)
data2 = numpy.linspace(0, 10, 500)

D1fixedx = Dxt(A1, k1, omega1, phisquare1, 1, fixedx1, data)
D1fixedt = Dxt(A1, k1, omega1, phisquare1, 0, fixedt1, data2)
D2fixedx = Dxt(A2, k2, omega2, phisquare2, 1, fixedx2, data)
D2fixedt = Dxt(A2, k2, omega2, phisquare2, 0, fixedt2, data2)

sumfixedx = D1fixedx + D2fixedx
sumfixedt = D1fixedt + D2fixedt

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = matplotlib.pyplot.subplots(3, 2)

#Plot 1
ax1.plot(data, D1fixedx)
#Plot 2
ax2.plot(data2, D1fixedt)
#Plot 3
ax3.plot(data, D2fixedx)
#Plot 4
ax4.plot(data2, D2fixedt)
#Plot 5
ax5.plot(data, sumfixedx)
#Plot 6
ax6.plot(data2, sumfixedt)

#ShowsPlot
matplotlib.pyplot.show()

