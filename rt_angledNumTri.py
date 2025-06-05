
print("________________________________________________________")
print("Right Angled Number Triangle")
print("________________________________________________________")

while True:
    height = int(input("Enter the height (positive value) of the triangle: "))
    if height > 0:
        break

print("________________________________________________________")

for i in range(0, height):
    for j in range(0, i+1):
        print(i+1, end=" ")
    print("")

print("________________________________________________________")