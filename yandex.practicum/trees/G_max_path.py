# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

result = []


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if root is None:
        return 0
    result.append(root.value)
    if root.value < 0:
        result.clear()
    solution(root.left)
    solution(root.right)
    return sum(result)


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()