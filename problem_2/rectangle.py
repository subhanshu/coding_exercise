class Rectangle:
    x1 =0
    y1 =0
    x2 =0
    y2 =0

    def __init__(self, x1,y1,x2,y2):
        if type(x1) not in [int, float] or type(y1) not in [int, float] or type(x2) not in [int, float] or type(y2) not in [int, float]:
            raise TypeError("Points should be numbers only")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def to_string(self):
        return "(" + str(self.x1) + "," + str(self.y1) + ")," + "(" + str(self.x2) + "," + str(self.y2) + ")"

    #Checks if the point (px,py) is inside a rectangle
    def is_point_inside_rect(self, px, py):
	    return (self.x1 < px < self.x2) and (self.y1 < py < self.y2)
        

    def is_covered(self, rect):
        """ check if the given rectange is covered by this one returns the following
            False: if not covered
            COVERED: if fully covered
            PARTIALLY_COVERED: if part of a rectangle is inside this one
        """
        #check if all four pints of the rectangle falls inside this rectangle
        #(x1,y1) (x1,y2) (x2,y2), (x2,y1)  

        if type(rect) is not type(self):
            raise TypeError("Only objects of class Rectangle can be checked")

        p1 = self.is_point_inside_rect(rect.x1, rect.y1)
        p2 = self.is_point_inside_rect(rect.x1, rect.y2)
        p3 = self.is_point_inside_rect(rect.x2, rect.y2)
        p4 = self.is_point_inside_rect(rect.x2, rect.y1)

        if p1 and p2 and p3 and p4 :
            result = "COVERED"
        elif p1 or p2 or p3 or p4 :
            result = "PARTIALLY_COVERED"
        elif not(p1 or p2 or p3 or p4) :
            result = False
        return result