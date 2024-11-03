from itertools import permutations

def find_sequences(m, numbers):
    sequences = set(permutations(numbers, m))
    sorted_sequences = sorted(sequences)
    for seq in sorted_sequences:
        print(" ".join(map(str, seq)))

if __name__ == "__main__":
    n,m = map(int, input().split())
    numbers = list(map(int, input().split()))
    find_sequences(m, numbers)
