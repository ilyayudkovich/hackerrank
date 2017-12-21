#!/bin/python2

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    print root.data,

    if root.right:
        preOrder(root.right)
    if root.left:
        preOrder(root.left)

def postOrder(root):

    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)

    print root.data,

def inOrder(root):
    if root:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)

def height(root):
    if not root:
        return -1
    else:
        return max(height(root.left), height(root.right)) + 1


def topView(root):
    def goLeft(root):
        if root:
            goLeft(root)
            print root.data,

    def goRight(root):
        if root:
            print root.data,
            goRight(root)

    goLeft(root)
    goRight(root.right)

def printTreeGivenLevel(root, level):
    if not root:
        return
    if level is 1:
        print root.data,
    elif level > 1:
        printTreeGivenLevel(root.left, level - 1)
        printTreeGivenLevel(root.right, level - 1)

def levelOrder(root):
    h = height(root)
    for i in range(0, h + 2):
        printTreeGivenLevel(root, i) 



def insert(root, val):
    if not root:
        return Node(val)

    if root.data > val:
        if not root.left == None:
            insert(root.left, val)
        else:
            root.left = Node(val)

    elif root.data <= val:
        if not root.right == None:
            insert(root.right, val)
        else:
            root.right = Node(val)

    return root


