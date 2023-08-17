# Motion Equations (uvats equations) solver

The script uvats.py can be used to solve the age old problems that physics and applied maths secondary students come across. workings.py lists all the possible combinations of unknowns and their solutions. minusB.py contains the working of the minus b formula used to get the roots of a quadratic equation used in one of the solutions in workings.py. minusTest.py is a file used for rough work and testing and holds no value to the final output.

The following are known as the motion equations (or uvats equations):

- v = u + at
- v<sup>2</sup> = u<sup>2</sup> + 2as
- s = ut + 1/2at<sup>2</sup>
- s = vt - 1/2at<sup>2</sup>
- s = 1/2(u + v)t

Using these formulae I have built the enclosed scripts to solve for the unknown values.

*Must knows:*
- There must be 3 knowns in order to solve for the other 2.
- There are combinations that aren't possible (ya know because of the laws of physics).
- If you find any problems with it please let me know and I'll look at fixing it.

The meaning of uvats:
- u = initial velocity
- v = final velocity
- a = acceleration (or deceleration, it will come up as a negative value)
- t = time taken
- s = displacement (sometimes referred to as distance)

# The minusB Formula for Quadratic Equations

I used it so much in secondary school that I thought creating a function that could help you solve a quadratic equation would be fun.

Quadratic Equation:
When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$ and they are 

$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$

using the method:

positiveRoot, negativeRoot = minusB(a, b, c)