modulo = 1000000
def factorial(n):
    """find the factorial of n."""
    result = 1
    for i in range(1, n+1):
        result = (result * i)
    return result

def combination(n, k):
    """find combination for given num object and sample."""
    return factorial(n) // (factorial(k) * factorial(n-k))

def num_isoforms(n, m):
    
    result = 0
    for i in range(m, n+1):
        result += combination(n, i)
    return result

with open("problems/rosalind_aspc.txt") as file:
    content = file.read()
    content = content.strip().split(" ")
    num_exon = int(content[0])
    min_exon = int(content[1])
    print(num_isoforms(num_exon, min_exon) % modulo)
# print(factorial(1927))
# print(9000000 % 1000000)

# print(2/5)
# print("%.50f" % (2/5))