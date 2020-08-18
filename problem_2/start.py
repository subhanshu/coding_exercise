#Assumptions 
# - The sides of the rectangle are aligned to x axis and y axis
# - If the the sides of the rectangle are just touching then its not being considered covered

from rectangle import Rectangle
import operator

rect1 = Rectangle(10,10,20,20)


#covered
rect2 = Rectangle(11,11,18,18)

#covered
rect3 = Rectangle(12,13,17,16)

#doesn't touch
rect4 = Rectangle(8,8,9,9)

#touches
rect5 = Rectangle(7,11,10,15)

#touches
rect6 = Rectangle(7,11,10,15)

#partially covered
rect7 = Rectangle(7,11,15,15)

#partially covered
rect8 = Rectangle(16,16,22,19)

rect_list = [rect2, rect3, rect4, rect5, rect6, rect7, rect8]

def main():
    #get list of partially covered or fully covered rectangles
    covered_rectangles =[]
    for x in rect_list:
        covered = rect1.is_covered(x)
        if covered == 'COVERED' or covered == 'PARTIALLY_COVERED':
            covered_rectangles.append(x)

    #sorted on x using bottom-left corner      
    covered_rectangles.sort(key=operator.attrgetter('x1'))
    print("sorted on x using bottom-left corner")
    for r in covered_rectangles:
        print(r.to_string())


    #sorted on y using bottom-left corner      
    covered_rectangles.sort(key=operator.attrgetter('y1'))
    print("sorted on y using bottom-left corner ")
    for r in covered_rectangles:
        print(r.to_string())

    #sorted on x using top-right corner      
    covered_rectangles.sort(key=operator.attrgetter('x2'))
    print("sorted on x using top-right corner ")
    for r in covered_rectangles:
        print(r.to_string())

    #sorted on y using top-right corner      
    covered_rectangles.sort(key=operator.attrgetter('y2'))
    print("sorted on y using top-right corner  ")
    for r in covered_rectangles:
        print(r.to_string())


if __name__ == '__main__':
    main()