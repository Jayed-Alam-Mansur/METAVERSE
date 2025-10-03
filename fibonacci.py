def print_fibonacci(n: int) -> None:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    N = int(input("Enter N: "))
    print_fibonacci(N)
