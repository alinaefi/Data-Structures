# python3
# Your task is to implement this first step and convert a given array of integers into a heap. You will
    # do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
    # elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap using
    # only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap instead
    # of a max-heap in this problem.
    # Input Format. The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
    # integers 𝑎𝑖.
    # Constraints. 1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109
    # All 𝑎𝑖 are distinct.
    # Output Format. The first line of the output should contain single integer 𝑚 — the total number of swaps.
    # 𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
    # to convert the array 𝑎 into a heap. Each swap is described by a pair of integers 𝑖, 𝑗 — the 0-based
    # indices of the elements to be swapped. After applying all the swaps in the specified order the array
    # must become a heap, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:
    # 1. If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
    # 2. If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.



def build_heap(data):
    """Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """

    def left_child(i):
        """returns index of the left child in binary tree"""
        return 2*i+1

    def right_child(i):
        """returns index of the right child in binary tree"""
        return 2*i+2

    def sift_down(i):
        """moves the element closer to the root"""
        max_index = i
        l = left_child(i)
        if (l < size and data[l] < data[max_index]):
            max_index = l
        r = right_child(i)
        if (r < size and data[r] < data[max_index]):
            max_index = r
        if i != max_index:
            data[i], data[max_index] = data[max_index], data[i]
            swaps.append((i, max_index))
            sift_down(max_index)
        return
    
    swaps = []
    size = len(data)
    for i in range(size//2-1, -1, -1):
        sift_down(i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
