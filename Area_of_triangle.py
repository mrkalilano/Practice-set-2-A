def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s *(s - a)*(s - b)*(s-c))** 0.5
    return area
    
a = int(input("Enter the side of a triangle: "))
b = int(input("Enter the side of a triangle: "))
c = int(input("Enter the side of a triangle: "))
    
result = calculate_area(a, b, c)
print(result)
