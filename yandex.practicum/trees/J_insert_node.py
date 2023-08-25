# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root: Node, key: int) -> Node:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if root is None:
        return Node(key)
    curr = root
    prev = None
    while curr is not None:
        prev = curr
        if key < curr.value:
            curr = curr.left
        else:
            curr = curr.right

    new_node = Node(key)

    if key < prev.value:
        prev.left = new_node
    else:
        prev.right = new_node

    return root
