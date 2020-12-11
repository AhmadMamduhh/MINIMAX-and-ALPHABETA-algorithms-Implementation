"""
Created on Fri Dec 11 

@author: Ahmed Mamdouh - 16P6020

"""
from random import randint

#  Some important constants
INFINITY = 999999999
NEGATIVE_INFINITY = -999999999

# Defining classes needed by the algorithm

class Node:
    """
    General class for node
    
    """
    def __init__(self, value):
        self.value = value


class NonLeafNode(Node) : 
    """
    This class represents all nodes that aren't leaf nodes. They contain other
    children nodes which could be leaf nodes or non-leaf nodes.
    
    """
    
    def __init__(self):
        super().__init__(0)
        self.children = []


class LeafNode(Node)  : 
    """
    This class represents all nodes that are leaf nodes. They don't contain
    children but they hold values which we will use to calculate the values
    of other nodes in the tree until we reach the root node.
    
    """
    def __init__(self, value = 0):
        super().__init__(value)
        

class Tree:
    """
    This class represents the tree in which MINIMAX will be applied to.
    It's defined by a root node which may or may not have children
    
    """
    def __init__(self, root_node):
        self.root_node = root_node
        
    def addChildNodeToRoot(self, node):
        self.root_node.children.append(node)

# Defining MINIMAX methods

def apply_minimax(tree): 
    """
    Parameters
    ----------
    tree : Tree
        the tree object we will apply minimax onto.

    Returns
    -------
    value: int
    the value at the root node of the tree.

    """
    value = get_max(tree.root_node)
    return value

def get_max(node): 
    """
    Takes as input a node and finds the maximum value of its children

    """
    
    if(isinstance(node, NonLeafNode)):
        maximum = NEGATIVE_INFINITY
        for n in node.children: 
            maximum = max(maximum, get_min(n))
            node.value = maximum
        return maximum

    else: # Recursion stopping condition
        return node.value

        
def get_min(node): 
    """
    Takes as input a node and finds the minimum value of its children

    """
    if(isinstance(node, NonLeafNode)): 
        minimum = INFINITY
        for n in node.children : 
            minimum = min(minimum, get_max(n))
            node.value = minimum
        return minimum
    
    else: # Recursion stopping condition
        return node.value

    
# Testing purposes for the algorithm
    
def initialize_simple_tree():
    """
    this function creates a simple binary tree with 3 levels: one root level
    and two more levels below it

    Returns
    -------
    tree : the constructed simple tree object
    
    """
    root_node = NonLeafNode()
    tree = Tree(root_node)
    node11 = NonLeafNode()
    node12 = NonLeafNode()
    node11.children.append(LeafNode(randint(0,51)))
    node11.children.append(LeafNode(randint(0,51)))
    node12.children.append(LeafNode(randint(0,51)))
    node12.children.append(LeafNode(randint(0,51)))
    tree.addChildNodeToRoot(node11)
    tree.addChildNodeToRoot(node12)
    
    return tree

def print_tree(tree):
    """
    This function takes a three level tree and prints it in the console
    
    """
    print("level 0:             " + str(tree.root_node.value))
    print('level 1:   ' + str(tree.root_node.children[0].value) + "                    "
          + str(tree.root_node.children[1].value))
    print('level 2: ' + str(tree.root_node.children[0].children[0].value) + "   "
          + str(tree.root_node.children[0].children[1].value) + "               "
          + str(tree.root_node.children[1].children[0].value) + "   "
          + str(tree.root_node.children[1].children[1].value))

def initialize_four_level_tree():
    """
    this function creates a simple binary tree with 4 levels: one root level
    and three more levels below it

    Returns
    -------
    tree : the constructed four-level tree object
    
    """
    root_node = NonLeafNode()
    tree = Tree(root_node)
    node11 = NonLeafNode()
    node12 = NonLeafNode()
    node21 = NonLeafNode()
    node22 = NonLeafNode()
    node23 = NonLeafNode()
    node24 = NonLeafNode()
    node11.children.append(node21)
    node11.children.append(node22)
    node12.children.append(node23)
    node12.children.append(node24)
    node21.children.append(LeafNode(randint(1,51)))
    node21.children.append(LeafNode(randint(1,51)))
    node22.children.append(LeafNode(randint(1,51)))
    node22.children.append(LeafNode(randint(1,51)))
    node23.children.append(LeafNode(randint(1,51)))
    node23.children.append(LeafNode(randint(1,51)))
    node24.children.append(LeafNode(randint(1,51)))
    node24.children.append(LeafNode(randint(1,51)))
    tree.addChildNodeToRoot(node11)
    tree.addChildNodeToRoot(node12)
    
    return tree

def print_tree_four_level(tree):
    """
    This function takes a three level tree and prints it in the console
    
    """
    print("level 0:                                " + str(tree.root_node.value))
    print('level 1:     ' + str(tree.root_node.children[0].value) + "                                            "
          + str(tree.root_node.children[1].value))
    print('level 2:  ' + str(tree.root_node.children[0].children[0].value) + "         "
          + str(tree.root_node.children[0].children[1].value) + "                             "
          + str(tree.root_node.children[1].children[0].value) + "               "
          + str(tree.root_node.children[1].children[1].value))
    print('level 3: ' + str(tree.root_node.children[0].children[0].children[0].value) + "   "
          + str(tree.root_node.children[0].children[0].children[1].value) + "   "
          + str(tree.root_node.children[0].children[1].children[0].value) + "   "
          + str(tree.root_node.children[0].children[1].children[1].value) + "                       " 
          + str(tree.root_node.children[1].children[0].children[0].value) + "   "
          + str(tree.root_node.children[1].children[0].children[1].value) + "           "
          + str(tree.root_node.children[1].children[1].children[0].value) + "    "
          + str(tree.root_node.children[1].children[1].children[1].value))

def main():
    """
    Testing my implementation on a simple tree
    
    """
    tree = initialize_simple_tree()
    print("BEFORE MINIMAX")
    print_tree(tree)
    apply_minimax(tree)
    print()
    print()
    print("AFTER MINIMAX")
    print_tree(tree)
    
    print()
    print("-" * 40)
    print()
    
    tree_four_level = initialize_four_level_tree()
    print("BEFORE MINIMAX")
    print_tree_four_level(tree_four_level)
    apply_minimax(tree_four_level)
    print()
    print()
    print("AFTER MINIMAX")
    print_tree_four_level(tree_four_level)
main()
    
    
    
    
    
    
    