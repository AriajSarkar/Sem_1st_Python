# Importing the array module
import array

# Creating an array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])

# Displaying the original array
print("Original Array:", numbers)

# Accessing elements in the array
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Adding elements to the array
numbers.append(60)
print("Array after appending 60:", numbers)

# Inserting an element at a specific position
numbers.insert(2, 25)  # Inserts 25 at index 2
print("Array after inserting 25 at index 2:", numbers)

# Removing an element
numbers.remove(40)
print("Array after removing 40:", numbers)

# Updating an element
numbers[1] = 15
print("Array after updating index 1 to 15:", numbers)

# Iterating through the array
print("Iterating through the array:")
for num in numbers:
    print(num, end=' ')
print()

# Finding the length of the array
print("Length of the array:", len(numbers))
