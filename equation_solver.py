import math

def solve_equation(a, b, c):
    
    if a == 0:
      print("a = 0 :This is not a 2nd degree equation.")

    D = (b ** 2 - 4 * a * c) ** 0.5        
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    print('x1 : {0}'.format(x1))
    print('x2 : {0}'.format(x2))
    # Your solution here
    # To compute a square root use math.sqrt(number)
    # To return two values from a function, you can separate them using a comma: return x1, x2
    

# You can use the following examples to test your implementation
solve_equation(1, -1, -6)
solve_equation(3, 42, 39)
solve_equation(1,  0, -4)
solve_equation(1,  0,  0)
solve_equation(0,  1, -5)
solve_equation(1,  1,  1)