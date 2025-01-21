def solution(sizes):
    answer = 0

    # 각 명함의 가로, 세로를 회전하여 큰 값은 큰 값끼리, 작은 값은 작은 값끼리 비교
    answer = max(max(i) for i in sizes) * max(min(i) for i in sizes)
    return answer