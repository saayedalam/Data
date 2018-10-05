 class Box(object):
        """Represents a box
        attributes: length, width"""
        
        def __init__(self, length = 0, width = 0):
            self.length = length
            self.width = width
            
        def render(self, other):
            """a box with asterisks of length and width dimensions"""
            for i in range(1, self.length+1):
                for j in range(1, self.width+1):
                    if (i == 1 or i == self.length or
                        j == 1 or j == self.width):
                        print(".", end="")
                    else:
                        print(" ", end="")
                print()
        
        def invert(self):
            """switches length and width with each other"""
            self.width = self.length
            self.width = self.length
                   
        def get_area(self):        
            """area of a box"""
            return self.length * self.width
        
        def get_perimeter(self):
            """perimeter of a box"""
            return 2 * (self.length + self.width)
        
        def double(self):
            """doubles the size of the box"""
            self.length = 2 * self.length
        
        def __eq__(self, other):
            """two boxes are equal if their respective 
            lengths and widths are identical"""
            if self.length == other.length and self.width == other.width:
                return True
            else:
                return False
         
        def print_dim(self):    
            """prints to screen the length and width details of the box"""
            print("Length of the box is " + str(self.length) + "\n" + 
                  "Width of the box is " + str(self.width))
            
        def get_dim(self):
            """returns a tuple containing the length and width of the box"""
            return '%d, %d' % (self.length, self.width)
        
        def combine(self, other):
            """takes another box as an argument and increases the length and 
            width by the dimensions of the box passed in"""
            other.length += self.length
            other.width += self.width
        
        def get_hypot(self):
            """finds the length of the diagonal that cuts throught the middle"""
            c = (self.length**2 + self.width**2)**(1/2)
            return round(c)
        
    #Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively 
    box1 = Box(5, 10)
    box2 = Box(3, 4)
    box3 = Box(5, 10)
    
    #Print dimension info for each using print_dim()
    box1.print_dim()
    box2.print_dim()
    box3.print_dim()
    
    #Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
    box1 == box2
    box1 == box3
    
    #Combine box3 into box1 (i.e. box1.combine())
    box1.combine(box3)
    
    #Double the size of box2
    box2.double()
    
    #Combine box2 into box1
    box1.combine(box2)
