import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, list(input())))
    counter = [0 for _ in range(10)]
    max_val = 0
    for num in numbers:
        counter[num] += 1
        if num > max_val and counter[num] >= counter[max_val]:
            max_val = num

    print(f'#{tc} {max_val} {counter[max_val]}')
