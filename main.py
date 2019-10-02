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
    if node:
        return "%s,%s,%s" % (node.val,
                               serialize(node.left),
                               serialize(node.right))
    return 'None'


def deserialize(string):
    """recursive deserialization using nested function"""
    the_list = string.split(',')
    list_len = len(the_list)
    idx = 0

    def r_deserialize():
        """recursive deserializer nested function"""
        nonlocal idx
        if list_len > idx + 1:
            idx += 1
            if the_list[idx - 1] != 'None':
                return Node(the_list[idx - 1], r_deserialize(), r_deserialize())
            return None
        return None

    return r_deserialize()


print(deserialize(serialize(Node('root', Node('left', Node('left.left')),
                                 Node('right')))).left.left.val)
