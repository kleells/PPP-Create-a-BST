#Part 1: Create a BSTNode class

class BSTNode:
  # The constructor should accept up to three arguments: data, left,
  # and right
    # If any of the arguments are not specified, they should
    # default to None.
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
  
  # Write two magic methods (__str__() and __repr__() ) to allow
  # the nodes to be printed. These two magic methods should
  # return strings that represent the node. They should both
  # return the same thing, the value of the node's data as a string.
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)

#Part 2: Create a BST class
# Create a BST class that fulfills the following requirements:
  # The constructor should accept one argument, root.

  # If root is not specified, it should default to None
class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []

  # Write two magic methods (__str__() and __repr__() ) to allow the
  # tree to be printed. These two magic methods should return strings
  # that represent the nodes in the tree, printed in a readable format.
  # They should both return the same thing.
    # If the tree is empty, return "The tree is empty".

    # Otherwise, do the following:
      # Initialize a variable self.output to an empty string

      # Call the self.print_tree() function (given below)
      # with node set to root. Note that this function doesn't
      # return any value, but rather edits self.output as it runs.

      # Return the self.output variable
  def __str__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def __repr__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output

  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)

#Part 3: Add functionality to your BST class
# Using your understanding of BSTs and how they work,
# implement the add() method:
    # add(): This function should accept an int or a BSTNode
    # and add it to the BST.
  def add(self, node):
    # If the input is of any type other than BSTNode
    # or int, raise a ValueError
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must pass an int or a BSTNode")

    # If the input is an int, create a BSTNode with
    # that int as the value
    if type(node) == int:
      node = BSTNode(node)

    # If the node with the same value is already in the
    # tree, change nothing (adding a class attribute called self.contents
    # keeps track of the contents of the tree)
    if node.data in self.contents:
      return

    # If the tree is empty (root == None), set the root
    # equal to the new node.
    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

  # The node must be added in the correct spot (larger
  # numbers as right children of root, smaller children
  # as left) on the tree. Use a helper function,
  # add_node(), to do this. The helper function should
  # accept a "current node" as well as the "new node"
  def add_node(self, cur_node, new_node):
    # If the new node is bigger than the current node,
    # recursively call the helper function with
    # current.right. If the new node is bigger than the
    # current node, recursively call the helper function with
    # current.left. Continue traversing this way until the
    # spot in the direction you want to go is empty.
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.right, new_node)
    else: #new node smaller, go left
      if cur_node.left == None:
        cur_node.left = new_node
        self.contents.append(new_node.data)
        return
      # When you find that the direction you want to go is
      # empty, set the current node's correct direction equal
      # to the new node to add it.
      else:
        self.add_node(cur_node.left, new_node)

# TEST FOR PART ONE
node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5

# TEST FOR PART TWO
bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

# TEST FOR PART THREE
#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)