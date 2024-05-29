# Diagram Class

## Line

The `Line` class used to represent a Line in a diagram. 

### Attributes

- `color`(str): a formatted string to determine the color of the line (default is 'black')
- `arrow_type`(str): a formatted string to determine the type of the arrow (default is '->')
- `width`(str): a formatted string to determine the width of the line (default is '1.5pt')
- `line_type`(str): a formatted string to determine the type of the line (default is 'line')
- `x1, y1, x2, y2`(int): integers representing the coordinates of the line (default is (0,0) to (1,1))

### Methods

#### def generate_id(cls)
Generates a unique id for each line by incrementing a class variable 'id_counter'.
- Parameters: None
- Returns: A unique id for the line.

#### def get_style(self)
Returns the style of the line as a string.
- Parameters: None
- Returns: The style of the line as a string.

#### def draw(self)
Returns a string that represents the line in a format that can be used to draw it.
- Parameters: None
- Returns: A string that represents the line in a format that can be used to draw it.

## _Node_
An abstract base class that other classes can inherit from.

### Attributes
None

### Methods

#### def generate_id(cls)
Generates a unique id for each line by incrementing a class variable 'id_counter'.
- Parameters: None
- Returns: A unique id for the line.

#### def get_style(self)
Returns the style of the line as a string.
- Parameters: None
- Returns: The style of the line as a string.

#### def draw(self)
Returns a string that represents the line in a format that can be used to draw it.
- Parameters: None
- Returns: A string that represents the line in a format that can be used to draw it.

## Title
The `Title` class used to represent a title in a diagram.

### Attributes

- `text_width`(str): a formatted string to determine the width of the text (default is '')
- `text_position`(str): a formatted string to determine the position of the text (default is '')
- `text_align`(str): a formatted string to determine the alignment of the text (default is 'centered')
- `name`(str): a formatted string to determine the name of the tittle (default is '')
- `formula`(str): a formatted string to determine the formula of the tittle (default is '')

### Methods

#### def get_style(self)
Returns the style of the title as a string.
- Parameters: None
- Returns: The style of the title as a string.

#### def draw(self)
Returns a string that represents the title in a format that can be used to draw it.
- Parameters: None
- Returns: A string that represents the title in a format that can be used to draw it.
