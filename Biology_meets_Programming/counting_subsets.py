def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = (result * i)
    return result


def combination(r, n):
    return factorial(n) // (factorial(r) * factorial((n - r)))


def count_subsets(n):
    """Counts number of subsets in set that containing n elements"""

    result = 1
    modulo = 1000000
    for _ in range(n):
        result = (result * 2) % modulo  # result never can exceed 1000000
    return result


# print(count_subsets(868))
