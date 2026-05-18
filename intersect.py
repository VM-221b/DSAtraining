def intersect(a, b):
    return list(set(a) & set(b))

if __name__ == "__main__":
    a = list(map(int, input("Enter first list: ").split()))
    b = list(map(int, input("Enter second list: ").split()))

    res = intersect(a, b)

    print(*res)