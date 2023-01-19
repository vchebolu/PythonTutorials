try:
    length = float(input("Enter length of rectangle"))
    width = float(input("Enter width of rectangle"))

    area = length * width

    print(f"are of rectanlge is {area}")
except ValueError:
    print("Please enter a number")