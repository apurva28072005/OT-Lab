import sympy as sp
# Define variable
x = sp.Symbol('x')

# Define function
f = x**3 - 6*x**2 + 9*x + 1

print("Function:", f)

# First derivative
f_prime = sp.diff(f, x)
print("\nFirst Derivative:",f_prime)

# Critical points
critical_points = sp.solve(f_prime, x)

# Second derivative
f_double = sp.diff(f_prime, x)

print("\nCritical Points Analysis:")

for point in critical_points:

  second_value = f_double.subs(x, point)

if second_value > 0:
  print(f"x = {point}: Local Minimum.")
elif second_value < 0:
  print(f"x = {point}: Local Maximum.")
else:
  print(f"x = {point}: Test Inconclusive")

