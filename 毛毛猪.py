from tqdm import tqdm

def gongyueshu(a, b, c):
    smallest = min(a, b, c)
    i = smallest
    while i > 0:
        if a % i == 0 and b % i == 0 and c % i == 0:
            return i
        i -= 1
    return False

for i in tqdm(range(62500)):
    for j in tqdm(range(62500)):
        k = (62500 - 14 * i - 21 * j) / 28
        if k % 1 == 0 and gongyueshu(i, j, k) != False:
            print(i, j, k)
            break
