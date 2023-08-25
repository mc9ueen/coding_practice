# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


first_tree = []
second_tree = []


def first_tree_round(root):
    if root is None:
        return
    first_tree_round(root.left)
    first_tree.append(root.value)
    first_tree_round(root.right)


def second_tree_round(root):
    if root is None:
        return
    second_tree_round(root.left)
    second_tree.append(root.value)
    second_tree_round(root.right)


def solution(root1, root2) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    first_tree_round(root1)
    second_tree_round(root2)
    return first_tree == second_tree


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()