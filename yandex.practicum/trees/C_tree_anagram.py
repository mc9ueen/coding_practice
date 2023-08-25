# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

left = []
right = []


def left_round(root):
    if root is None:
        return
    left_round(root.left)
    left.append(root.value)
    left_round(root.right)


def right_round(root):
    if root is None:
        return
    right_round(root.right)
    right.append(root.value)
    right_round(root.left)

def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    left_round(root.left)
    right_round(root.right)
    return left == right


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)

if __name__ == '__main__':
    test()