def solution(arr): #arr [1,1,3,3,0,1,1]
    answer = [arr[0]] # arr[0] 첫번째 원소를 저장
    for i in range(1, len(arr)): # 두 번째 원소  ~ 마지막 원소
        if arr[i] != arr[i-1]: #arr[i] : 현재 원소 arr[i-1] 이전원소
            answer.append(arr[i]) # 다르면 중복되지 않으므로 answer에 추가 
    return answer #[1,3,0,1]