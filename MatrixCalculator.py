import numpy

#input of vectors

a1 = numpy.array([-1,0,1,0,0])
a2 = numpy.array([5,0,0,5,0])
a3 = numpy.array([4,0,0,0,4])
A = [ a1, a2, a3 ]



print (A)

Q = []
assert(numpy.linalg.matrix_rank(A) == 3)

q = A[0] / numpy.linalg.norm(A[0])
Q.append(q)
print (q)

#output 1

q = A[1] - numpy.dot(Q[0],A[1])*Q[0]
q = q / numpy.linalg.norm(q)
Q.append(q)
print (q)

#output 2

q = A[2]
for j in range (0,2):
    q = q - numpy.dot(Q[j],A[2])*Q[j]
q = q / numpy.linalg.norm(q)
Q.append(q)
print (q)

#output 3

v = numpy.array([-9,0,3,10,-16])

print (v)
                
                
import sympy
from sympy.solvers import solve
from sympy import Symbol

from sympy import symbols, Eq, solve

x, y, z = symbols("x y z")
equation_1 = Eq((b1*x + b2*y +b3*z), v = numpy.array([-9,0,3,10,-16])

print("Equation 1:", equation_1)

solution = solve((equation_1), (x, y, z))
print("Solution:", solution)
