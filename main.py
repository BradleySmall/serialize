#!/usr/bin/python3
"""Seriealize and Deserialize a binary tree """


class Node:
    """provided node class"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    """recursively parse tree creating a string"""
    if not node:
        return "None"
    else:
        return "Node('%s', %s, %s)" % (node.val,
                                       serialize(node.left),
                                       serialize(node.right))


def deserialize(string):
    """This seems like a cheat. Probably a better choice over eval()"""
    return eval(string)


print deserialize( serialize(Node('root', Node('left', Node('left.left')),
                                  Node('right')))).left.left.val
