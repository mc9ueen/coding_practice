# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_height(root):
    if root is None:
        return 0

    return max(get_height(root.left), get_height(root.right)) + 1


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if not root:
        return True

    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False

    return solution(root.left) and solution(root.right)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
