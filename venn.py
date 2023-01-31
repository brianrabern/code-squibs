import numpy as np
import matplotlib.pyplot as plt


class Circle():
    def __init__(self,a,b,r):
        self.a = a
        self.b= b
        self.r = r

    def area(self):
        return self.r**2*3.14

    def perimeter(self):
        return 2*self.r*3.14

    def circ_points(self):
        l = []
        left=(self.a-self.r)-1
        right=(self.a+self.r)+1
        bottom=(self.b-self.r)-1
        top=(self.b+self.r)+1

        for x in np.arange(left,right,.1):
            for y in np.arange(bottom,top,.1):
                g=round(((x-self.a)**2) + ((y-self.b)**2),1)
                if  g == self.r**2:
                   l.append([x,y])
        return l

NewCircle = Circle(0,0,6)

print(NewCircle.circ_points())

# for i in NewCircle.circ_points():

# plt.plot(NewCircle.circ_points()[0])
# plt.show()




# print(NewCircle.circ_points())
