# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)
    for i in range((n - 1) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(data)

    if right_child <= n - 1 and data[right_child] < data[min_index]:
        min_index = right_child

    if left_child <= n - 1 and data[left_child] < data[min_index]:
        min_index = left_child

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)

def main():

    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    choose = input()
    if "F" in choose:
        filename = input()
        if "a" not in filename:
            with open("tests/" + filename, 'r') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
                assert len(data) == n
                swaps = build_heap(data)
    elif "I" in choose:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
