from bst import *

def convert_to_tree(ls: list) -> BST:
    """
    Tree Sort: Takes in a (possibly unsorted) list and converts it to a binary search tree
    """
    tree= BST()
    for item in ls:
        tree.insert(item)
    return tree


def traversal(node: BSTNode) -> list:
    """
    Accept a tree node and perform an in-order depth-first traversal of the tree to get (what should be) a sorted list.
    """
    empty_list=[]
    def order_it(node):
        if node is not None:
         order_it(node.left)
         empty_list.append(node.data)
         order_it(node.right)
    order_it(node)
    return empty_list

def tree_sort(ls: list) -> list:
    make_tree = convert_to_tree(ls)
    return traversal(make_tree.root)
