import time
import random
import string

size = 1000000

# Experimenting with creating my own hashmap
# List lookup = O(n)
# Binary search tree lookup = O(log n)
# Hash map = O(1) + list lookup in smaller bin

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

hash_limit = 4096

b = [[] for _ in range(hash_limit)]
all_strings = []
print(b)

for _ in range(size):
    random_string = get_random_string(random.randint(10, 20))
    all_strings.append(random_string)
    index = hash(random_string) % hash_limit
    b[index].append(random_string)

print(b)

now = time.time()
for selection in all_strings:
    selection in b[hash(selection) % hash_limit]

print(f"{((time.time() - now) * 1000):.8f} ms")