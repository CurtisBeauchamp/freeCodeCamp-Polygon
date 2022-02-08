class Rectangle(object):
    
    def __init__(self, width=0, height=0):
        self.width  = width
        self.height = height
        
    def __repr__(self):
        official_string = f"Rectangle(width={self.width}, height={self.height})"
        return official_string
        
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height
        
    def get_area(self):
        area = self.width * self.height
        return area
        
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter
    
    def get_diagonal(self):
        diagonal = (pow(self.width, 2) + pow(self.height, 2)) ** 0.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50: return "Too big for picture."
        else:
            picture = ((("*" * self.width) + "\n") * self.height) 
            return picture
        
    def get_amount_inside(self, shape):
        times_fits_inside = (self.width // shape.width) * (self.height // shape.height)
        return times_fits_inside
    
    
class Square(Rectangle):
    
    def __init__(self, side_size):
        self.set_side(side_size)
        
    def __repr__(self):
        official_string = f"Square(side={self.width})"
        return official_string
    
    def set_height(self, new_height):
        return self.set_side(new_height)
    
    def set_width(self, new_width):
        return self.set_side(new_width)
    
    def set_side(self, side=0):
        super().set_width(side)
        super().set_height(side)