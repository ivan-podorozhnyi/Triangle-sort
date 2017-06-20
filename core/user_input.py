from core.triangle import add_triangle, triangles_list


def input_start():
    print("Please input the parameters of triangle:")
    name = input("<name>\n")
    try:
        a = float(input("<A side length>\n"))
        b = float(input("<B side length>\n"))
        c = float(input("<C side length>\n"))
        add_triangle(name, a, b, c)
    except ValueError:
        print("Side length value must be a number and can't be empty!")
        return
    answer = (input("Do you want to add one more triangle? (y/n)\n")).lower().strip()
    if answer == "y" or answer == "yes":
        input_start()
    else:
        print("==========Triangles list:==========")
        for trn in (sorted(triangles_list, key=lambda triangle: triangle.area, reverse=True)):
            print("[Triangle %s]: %f cm" % (trn.name, trn.area))
