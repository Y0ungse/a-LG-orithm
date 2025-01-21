# 여벌 옷 reserve
# 도난 당함 lost 
# 전체 학생 수 n
def solution(n, lost, reserve):
    # 오름차순 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve의 중복 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기
    # 나의 앞 번호부터 확인(앞번호나 뒷번호 중 한 명이 빌려주면 되므로 작은 번호부터 체크
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)   