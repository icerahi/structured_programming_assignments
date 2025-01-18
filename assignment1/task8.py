#Task 8: Volume and Surface Area of a Cylinder


def main(radius:int,height:int):
    pi= 3.14159
    volume= pi*radius**2*height 
    surface_area=2*pi*radius*(radius+height)
    print(f"Volume: {volume}\nSurface Area: {surface_area}")
    
main(int(input("Enter Volume:")),int(input("Enter Height:")))