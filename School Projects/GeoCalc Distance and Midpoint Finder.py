import math
x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))
x2 = int(input("enter x2: "))
y2 = int(input("enter y2: "))
subtractx = x2 - x1
subtracty = y2 - y1
add_x = x1 + x2
add_y = y1 + y2
divide_x = add_x / 2
divide_y = add_y / 2
pow1 = subtractx ** 2 
pow2 = subtracty ** 2
add_values = pow1 + pow2

square_root = math.sqrt(add_values)


print("your distance is: " + str(square_root) +" / your points are (" + str(x1) + ","+ str(y1) + ") (" + str(x2) + "," + str(y2) + ")")
print("your midpoint is: (" + str(divide_x) + "," + str(divide_y) + ")" )