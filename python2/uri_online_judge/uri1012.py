from cmath import pi
 
# a=input().split(' ')
a=[ float(a) if '.' in a else int(a) for a in input().split(' ')]
A=a[0]
B=a[1]
C=a[2]
pi=3.14159

triangle=1.0/2*A*C
print("TRIANGULO: {:.3f}".format(triangle))
circle=pi*(C*C)
print("CIRCULO: {:.3f}".format(circle))
trapezium=((A+B)/2) * C
print("TRAPEZIO: {:.3f}".format(trapezium))
area_square=B*B
print("QUADRADO: {:.3f}".format(area_square))
rectangle=A*B
print("RETANGULO: {:.3f}".format(rectangle))


