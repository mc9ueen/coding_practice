# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


current_max_node = []
results = []


def solution(root) -> bool:
    current_max_node.append(root.value)
    if root.left:
        if root.value > root.left.value and root.left.value < current_max_node[-1]:
            current_max_node.append(root.value)
            if root.left.right:
                results.append(False if root.left.right.value >= current_max_node[0] else True)
            solution(root.left)
        else:
            results.append(False)
    if root.right:
        if root.value < root.right.value and root.right.value > current_max_node[-1]:
            current_max_node.append(root.value)
            if root.right.left:
                results.append(False if root.right.left.value <= current_max_node[0] else True)
            solution(root.right)
        else:
            results.append(False)
    print(current_max_node)
    print(results)
    return all(results)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
