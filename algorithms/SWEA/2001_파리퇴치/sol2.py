import sys
sys.stdin = open('input.txt')


# 파리채 한번 휘둘렀을 때의 총 합
def hit(r_idx, c_idx, size):
    total = 0
    for r in range(size):
        for c in range(size):
            total += matrix[r_idx + r][c_idx + c]

    return total


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    results = []

    for row in range(N-M+1):
        for col in range(N-M+1):
            total = hit(row, col, M)  # => 내리쳤을 때 잡은 파리 수를 return
            results.append(total)
    print(results)
    ans = max(results)

    print(f'#{tc} {ans}')
