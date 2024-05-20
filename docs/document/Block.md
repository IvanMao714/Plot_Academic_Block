# Block Class

## NeuralUnit

The `NeuralUnit` class represents a unit in a neural network. It consists of nodes, lines and titles.

### Attributes
- `neural_node`: The nodes in the neural network.
- `neural_line`: A list of lines in the neural network.
- `neural_title`: The title of the neural network.

### Methods

#### def add_node(self, node):
Adds a node to the NeuralUnit. If the current node is not a list, it converts it to a list before adding.
- Parameters: node (`NeuralNetworkNode`): The node to be added.
- Returns: None

#### def add_line(self, line):
Adds a line to the NeuralUnit. If the current line is not a list, it converts it to a list before adding.
- Parameters: line (`NeuralNetworkLine`): The line to be added.
- Returns: None

#### def add_title(self, title):
Sets the title of the NeuralUnit.
- Parameters: title (`NeuralTittle`): The title of the NeuralUnit.
- Returns: None

#### def get_style(self):
 Returns the style of the NeuralUnit as a string. The style is a combination of the styles of the node, line and title.
- Parameters: None
- Returns: The style of the NeuralUnit as a string.

#### def draw(self):
Draws the NeuralUnit by adding pins to the node and returning the drawn node and title.
- Parameters: None
- Returns: The drawn node and title(Latex format).

##### Example:
```python
line_list = [NeuralLine('in', '\\frac{\partial L}{\partial y_1}', 'left', '35pt'),
                 NeuralLine('out', '\\frac{\partial L}{\partial x_1}=\\frac{\partial L}{\partial y_1}\\frac{\partial y_1}{\partial x_1}','above right', '35pt'),
                 NeuralLine('out', '\\frac{\partial L}{\partial x_2}=\\frac{\partial L}{\partial y_1}\\frac{\partial y_1}{\partial x_2}', 'below right', '35pt')]
nu = NeuralUnit(NeuralNode(0, 0, 'A', '\diff f'), line_list,
                    NeuralTittle('200pt', '4pt of A', 'centered', '2', 'Node Unit'))
generate_doc([nu])
```
![neural_unit_example](../fig/neuralunit_example.jpg)

## NeuralLineLayer

The `NeuralLineLayer` class represents a layer of connections (lines) in a neural network diagram. Each instance of this class connects a 'front' layer of nodes to a 'behind' layer of nodes.

> [!CAUTION]
> 
> This class is not meant to be used directly. It is used by the [NeuralNetwork](./Diagram.md/#neuralnetwork) class to create the lines in the neural network diagram.



### Attributes
- `front_layer`(NeuralNodeLayer): The layer of nodes that the lines in this layer will start from.
- `behind_layer`(NeuralNodeLayer): The layer of nodes that the lines in this layer will end at.

### Methods

#### def get_style(self):
Returns the style of the lines in this layer as a string.
- Parameters: None
- Returns: The style of the lines in this layer as a string.

#### def draw(self):
Returns a string that represents the lines in this layer in a format that can be used to draw them.
- Parameters: None
- Returns: A string that represents the lines in this layer in a format that can be used to draw them.

## NeuralNodeLayer
The `NeuralNodeLayer` class represents a layer of nodes in a neural network diagram. Each instance of this class represents a layer of nodes, with each node having a specific type and number.

> [!CAUTION]
> 
> This class is not meant to be used directly. It is used by the [NeuralNetwork](./Diagram.md/#neuralnetwork) class to create the lines in the neural network diagram.

### Attributes
- `node_type`(NeuralNode): The type of nodes in this layer.
- `node_number`(Integer): The number of nodes in this layer.
- `horizon`(Double): The horizontal distance between the nodes in this layer.The horizon of the neural network. The horizon value is used to determine y-axis position of the nodes in the diagram. If the horizon is not specified, the nodes are placed on the top of the diagram. As below is the figure of horizon function.
![horizon](../fig/horizon_comparation.png)
- `front_layer`(NeuralNodeLayer): The layer in front of this layer. Default is None.

### Methods

#### def get_style(self):
Returns the style of the lines in this layer as a string.
- Parameters: None
- Returns: The style of the lines in this layer as a string.

#### def calculate_height(self):
Calculates and returns the height of this layer.
- Parameters: None 
- Return: The height of this layer.
- Raises ValueError: If the horizon is None.

#### def draw(self):
Returns a string that represents the lines in this layer in a format that can be used to draw them.
- Parameters: None
- Returns: A string that represents the lines in this layer in a format that can be used to draw them.
