def read_data():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    n = int(lines[0])
    m = int(lines[1])

    sorted_arr = lines[2].split()
    sorted_arr = list(map(int, sorted_arr))

    int_arr = lines[3].split()
    int_arr =  list(map(int, int_arr))

    return n, m, sorted_arr, int_arr

def binary_search(n, arr, target):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == '__main__':
    n, m, sorted_arr, int_arr = read_data()
    idx_arr = []

    for num in int_arr:
        idx = binary_search(n, sorted_arr, num)
        idx_arr.append(idx)

    print(" ".join(map(str, idx_arr)))