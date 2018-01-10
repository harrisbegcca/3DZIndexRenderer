from math import *
import math

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
import plotly

print("Calculus Project");
def g(s):
	return ("-2/((1/sqrt(2))+(%s/sqrt(2))**2)-1" % (s))

def f(s):
	return ("3*sin((%s-1)/8)*cos((%s-1)/8)" % (s,s))

yvals = []
bottom = []
xvals=[]
zval = []

print("Left Hand: ")
i = float(-2.5000)
sum = float(0)
sumv = float(0)
trap = []
zs = []
zs1 = []
top = []
ybefore = []
yafter = []


while (i<3.5):
	xvals.append(i)

	val = (eval(f(i))-eval(g(i)))
	yvals.append(val)
	sum+= val
	bottom.append(eval(g(i)))
	top.append(eval(f(i)))
	sumv+=val**2
	temp = float(6)/float(32);
	i += (temp)

i = 0
while (i<32):
	trap.append(bottom[i] + (yvals[i]/2))
	i +=1

i = 0
zval1=[]
while (i<32):
	
	zs.append((yvals[i]/2) * math.sqrt(3))
	zval.append(0)
	zval1.append((yvals[i]/2) * math.sqrt(3)* float(0.5))
	ybefore.append(trap[i] - yvals[i]/4)
	yafter.append(trap[i] + yvals[i]/4)
	i += 1



#print("Area: " + str(sum * (float(6)/float(32))) )
#print("Volume: " + str(sumv * (float(3*math.sqrt(3))/16)*(float(6)/float(32))))

trace0 = go.Scatter3d(
	x = xvals,
    y = ybefore,
    z = zval1
	)

trace = go.Scatter3d(
	x = xvals,
    y = yafter,
    z = zval1
	)

#trace1 = go.Scatter3d(
    #x = xvals,
    #y = trap,
    #z = zs
#)


trace3 = go.Scatter3d(
    x = xvals,
    y = top,
    z = zval
)

trace4 = go.Scatter3d(
    x = xvals,
    y = bottom,
    z = zval
)

layout = dict(title = 'Calculus Cross Sections',
              xaxis = dict(title = 'X'),
              yaxis = dict(title = 'Y'),
              margin=go.Margin(
        		l=-2,
        		r=2,
        		b=-2,
        		t=2,
        		pad=1
    			),
              )

data=[trace,trace0,trace3,trace4]
fig = dict(data=data, layout=layout)
py.plot(fig, filename='simple-3d-scatter')