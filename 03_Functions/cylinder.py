import math

def circle_area(diameter):
    """Returns the area of the circle
    at the base of the cylinder"""
    return 0.25*(math.pi)*(diameter**2)

def cylinder_volume(diameter, height):
    """Returns the volume of the cylinder"""
    return circle_area(diameter)*height

def main():
    """Requests diameter and height from the user
    and prints out the volume"""
    d = eval(input("Enter diameter:\n"))
    h = eval(input("Enter height:\n"))
    A = circle_area(d)
    V = cylinder_volume(d,h)
    print("The volume of the cylinder is {:.2f}".format(V))

if __name__=='__main__':
    main()
