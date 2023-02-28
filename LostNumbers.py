
n = int(input("Enter int: "))
distances = list(map(int, input().split()))

lineup = [0] * n
lineup[0] = 1  # Jimmy is always first

for i, dist in enumerate(distances):
    lineup[i + dist] = i + 2

print(' '.join(map(str, lineup)))

