class Rectangle:

  def __init__(self, width = 0, height = 0):
    self._width = width
    self._height = height 

  def __str__(self):
    return "Rectangle(width=" + str(self._width) + ", height=" + str(self._height) + ")"
    
# set_width
  def set_width(self, width):
    self._width = width

    
# get_width 
  def get_width(self):
    return self._width
    
# set_height
  def set_height(self, height):
    self._height = height

# get_height
  def get_height(self):
    return self._height

# get_area: Returns area (width * height)
  def get_area(self):
    return self._width * self._height
  
# get_perimeter: Returns perimeter (2 * width + 2 * height)
  
  def get_perimeter(self):
    return 2 * self._width + 2 * self._height
    
# get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
  
  def get_diagonal(self):
    return ((self._width ** 2 + self._height ** 2) ** .5)
    
# get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
  
  def get_picture(self):
    if self._width > 50 or self._height > 50:
      return "Too big for picture."
    else:
      picture = ""
    
      for h in range(self._height):
      
        picture += "".ljust(self._width, "*") + '\n'
      return picture
 
# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

  def get_amount_inside(self, shape):

    x_width = int(self._width / shape._width)
    x_height = int(self._height / shape._height)
    amount_inside = x_width * x_height

    return amount_inside

class Square(Rectangle):
  
  def __init__(self, side = 0):
    self._width = side
    self._height = side 
   
  def __str__(self):  
    return "Square(side=" + str(self._width) + ")"
    
  def set_side(self, side):
    self._width = side
    self._height = side 

  
  
   
   
