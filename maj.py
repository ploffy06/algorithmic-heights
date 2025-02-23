from collections import Counter

def read_data():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    lines = [list(map(int, line.replace("\n", "").split())) for line in lines]

    sizes = lines[0]
    arrs = lines[1:]

    return sizes[0], sizes[1], arrs

def majority_element(A, threshold):
    counter = Counter(A)
    most_common, count = counter.most_common(1)[0]

    return most_common if count > threshold else -1

def majority_element_entries(arrs, k):
    majority_elements = []
    for a in arrs:
        majority_elements.append(majority_element(a, k // 2))

    return majority_elements

if __name__ == '__main__':
    n, k, arrs = read_data()
    majority_elements = majority_element_entries(arrs, k)
    print(" ".join(list(map(str, majority_elements))))