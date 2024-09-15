print("How many elements do you want to store?:", end="")
size = int(input())
array = []  # declaration of array
print("\nEnter", size, "elements:\n")
for i in range(size):
    element = int(input())
    array.append(element)

print("The array is:")
for i in range(size):
    print(array[i], end=" ")  

