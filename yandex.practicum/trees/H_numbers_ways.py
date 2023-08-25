# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def dfs(root: "Node", path: list, paths: list):
    if root is None:
        return
    path.append(str(root.value))

    if root.left is None and root.right is None:
        paths.append(path.copy())
    else:
        dfs(root.left, path, paths)
        dfs(root.right, path, paths)
    path.pop()


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    paths = []
    dfs(root, [], paths)
    res = []
    for p in paths:
        tmp_str = ""
        for i in p:
            tmp_str += i
        res.append(tmp_str)
    res = (list(map(int, res)))
    return sum(res)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()
