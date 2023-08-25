def sift_up(heap, idx) -> int:
    if idx == 1:
        return 1
    parent_index = idx // 2
    if heap[parent_index] < heap[idx]:
        swap(heap, parent_index, idx)
        return sift_up(heap, parent_index)
    else:
        return idx


def swap(arr, current_index, needed_index):
    tmp = arr[current_index]
    arr[current_index] = arr[needed_index]
    arr[needed_index] = tmp


def test():
    size = int(input())
    sequence = [int(i) for i in input().split()]
    sequence = [-1] + sequence
    amount = int(input())
    indexes_values = [tuple(map(int, input().split())) for _ in range(amount)]
    for index, value in indexes_values:
        sequence[index] = sequence[index] + value
        result = sift_up(sequence, index)
        print(result)
    print(sequence)


if __name__ == '__main__':
    test()
