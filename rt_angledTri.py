
print("________________________________________________________")
print("Right Angled Triangle")
print("________________________________________________________")

while True:
    height = int(input("Enter the height (positive value) of the triangle: "))
    if height > 0:
        break

print("________________________________________________________")

for i in range(0, height):                        # Outer loop that iterates through the height of the triangle
    for j in range(0, i+1):                         # Nested loop that iterates through the width of the triangle
        print("*", end=" ")
    print("")

print("________________________________________________________")