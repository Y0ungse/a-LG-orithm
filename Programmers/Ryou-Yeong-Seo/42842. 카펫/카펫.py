def solution(brown, yellow):
    # 1. 전체 격자의 개수 계산
    total_tiles = brown + yellow

    # 2. 가능한 가로 길이 탐색 (가로는 세로보다 길거나 같아야 함)
    for height in range(3, int(total_tiles ** 0.5) + 1):  # 세로 최소 길이는 3부터 시작
        if total_tiles % height == 0:  # 전체 타일 수가 세로로 나누어 떨어지는 경우
            width = total_tiles // height  # 가로 길이 계산
            
            # 가로가 세로보다 길거나 같은 경우만 진행
            if width >= height:
                # 3. 테두리 갈색 타일과 중앙 노란색 타일의 조건 확인
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]
