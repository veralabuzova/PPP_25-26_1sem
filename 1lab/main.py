import random
N = 10
x = list(range(1, N+1))

def shuffle_cards(x):
    shuffled = x.copy()
    for i in range(len(shuffled)-1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

target_number = 7
position_counts = [0] * N

for _ in range(1000):
    shuffled = shuffle_cards(x)
    for position, number in enumerate(shuffled):
        if number == target_number:
            position_counts[position] += 1

print(f"\nСколько раз число {target_number} было на каждой позиции:")
for i in range(N):
    print(f"Позиция {i+1}: {position_counts[i]} раз")
