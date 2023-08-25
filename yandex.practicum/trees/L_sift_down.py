def sift_down(heap, idx) -> int:
    left = idx * 2
    right = idx * 2 + 1
    if len(heap) - 1 < left:
        return idx
    if right <= len(heap) - 1 and heap[left] < heap[right]:
        largest = right
    else:
        largest = left
    if heap[idx] < heap[largest]:
        swap(heap, idx, largest)
        return sift_down(heap, largest)
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
        sequence[index] = sequence[index] - value
        result = sift_down(sequence, index)
        print(result)
    print(sequence)


if __name__ == "__main__":
    test()
