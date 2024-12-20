def main():
    print("1. Find the Area of a Rectangle ")
    print("2. Find the Area of a Square ")
    print("3. Find the Area of a Circle ")
    print("4. Find the Area of a Triangle ")
    
    choice = int(input("Choose an operation: "))
    
    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is: ", length * width)
    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        print("The area of the square is: ", side * side)
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        result = 3.14 * radius * radius
        print("The area of the circle is: ", result)
    elif choice == 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        result = 0.5 * base * height
        print("The area of the triangle is: ", result)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()