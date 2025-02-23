def read_data():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    n = int(lines[0].replace("\n", ""))
    A = list(map(int, lines[1].replace("\n", "").split()))

    return n, A

def insertion_sort_swap_count(n, A):
    count = 0

    for i in range(1, n):
        k = i
        while k > 0 and A[k] < A[k - 1]:
            temp = A[k]
            A[k] = A[k - 1]
            A[k - 1] = temp

            count += 1
            k -= 1

    return A, count

n, A = read_data()
A, count = insertion_sort_swap_count(n, A)
print(count)