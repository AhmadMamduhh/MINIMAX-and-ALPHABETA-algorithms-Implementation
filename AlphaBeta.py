"""
Created on Sat Dec 12

@author: Ahmed Mamdouh - 16P6020

"""
from random import randint

#  Some important constants
INFINITY = 999999999
NEGATIVE_INFINITY = -999999999

# Global variables which keep track of count of cutoffs and count of cutoff leaf nodes
num_of_prunes = 0
num_of_leaves_bypassed = 0

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
        self.alpha = NEGATIVE_INFINITY
        self.beta = INFINITY
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

def get_max(node, beta = INFINITY): 
    """
    Takes as input a node and finds the maximum value of its children
    Also, takes beta of the parent node as a parameter to compare it to the
    alpha of the current node. if alpha >= beta then prunning occurs which
    causes a break as it is useless to continue calculation in this case.
    
    """
    global num_of_prunes
    global num_of_leaves_bypassed
    
    if(isinstance(node, NonLeafNode)):
        
        maximum = NEGATIVE_INFINITY
        for n in node.children: 
            
            if(node.alpha >= beta): # Pruning condition
                num_of_prunes += 1
                n.value = "X"
                if(isinstance(n, NonLeafNode)):
                    for child in n.children:
                        child.value = "X"
                        num_of_leaves_bypassed += 1
                else:
                    num_of_leaves_bypassed += 1
                break
            
            maximum = max(maximum, get_min(n, node.alpha))
            node.value = maximum
            if(maximum > node.alpha):
                node.alpha = maximum

            
        return maximum

    else: # Recursion stopping condition
        return node.value

        
def get_min(node, alpha = NEGATIVE_INFINITY): 
    """
    Takes as input a node and finds the minimum value of its children
    Also, takes alpha of the parent node as a parameter to compare it to the
    beta of the current node. if alpha >= beta then prunning occurs which
    causes a break as it is useless to continue calculation in this case.
    
    """
    global num_of_prunes
    global num_of_leaves_bypassed
    
    if(isinstance(node, NonLeafNode)): 
        minimum = INFINITY
        for n in node.children : 
            
            if(alpha >= node.beta): # pruning condition
                num_of_prunes += 1
                n.value = "X"
                if(isinstance(n, NonLeafNode)):
                    for child in n.children:
                        child.value = "X"
                        num_of_leaves_bypassed += 1
                else:
                    num_of_leaves_bypassed += 1
                break
            
            minimum = min(minimum, get_max(n, node.beta))
            node.value = minimum
            if(minimum < node.beta):
                node.beta = minimum
        return minimum
    
    else: # Recursion stopping condition
        return node.value

    
# Testing purposes for the algorithm
    
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
    node11.children.append(LeafNode(randint(1,51)))
    node11.children.append(LeafNode(randint(1,51)))
    node12.children.append(LeafNode(randint(1,51)))
    node12.children.append(LeafNode(randint(1,51)))
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

def main():
    """
    Testing my implementation on a simple tree
    
    """
    global num_of_prunes
    
    tree = initialize_four_level_tree()
    print("BEFORE ALPHABETA")
    print_tree_four_level(tree)
    print("Root node Alpha, Beta (BEFORE): " + str(tree.root_node.alpha) + ", " + str(tree.root_node.beta))
    apply_minimax(tree)
    print()
    print()
    print("AFTER ALPHABETA")
    print_tree_four_level(tree)
    print("Root node Alpha, Beta (AFTER): " + str(tree.root_node.alpha) + ", " + str(tree.root_node.beta))
    print("Number of prunes occurred: " + str(num_of_prunes))
    print("Number of leaf nodes not used: " + str(num_of_leaves_bypassed))
    
    
main()
    
    
    
    
    
    
    