# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
print("Enter the lengths of the three sides of a triangle (num):")
A = int(input('Enter side A of the triangle: '))
B = int(input('Enter side B of the triangle: '))
C = int(input('Enter side C of the triangle: '))

if A == B and A == C:
  print('This is an equilateral triangle.')
elif A != B and A != C and B != C:
  print('This is a scalene triangle.')
else:
  print('This is an isoceles')
