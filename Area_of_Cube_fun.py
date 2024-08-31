# 'Surface Area' is the total surface area of the cube

# 'Side'; is the length of one side of the cube
def area_of_cube():
    print("Enter the Side?")
    side = int(input())

    surface_area_cube = 6 * (side * side)

    print("The surface are of the cube is")
    print(surface_area_cube)
area_of_cube()