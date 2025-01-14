import heapq  # 파이썬 내장 힙 모듈

def solution(scoville, K):
    # 1. 스코빌 배열을 최소 힙으로 변환
    heapq.heapify(scoville)
    
    mix_count = 0  # 섞은 횟수 카운트
    
    # 2. 스코빌 섞기 과정 반복
    while len(scoville) > 1:  # 음식이 2개 이상 있어야 섞을 수 있음
        # 가장 맵지 않은 두 음식 꺼내기
        first = heapq.heappop(scoville)  # 가장 작은 값
        if first >= K:  # 가장 작은 값이 이미 K 이상이면 종료
            return mix_count
        
        second = heapq.heappop(scoville)  # 두 번째로 작은 값
        
        # 새로운 음식 만들기
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)  # 힙에 새 음식 추가
        
        mix_count += 1  # 섞은 횟수 증가
    
    # 3. 마지막 남은 음식 확인
    return mix_count if scoville[0] >= K else -1
