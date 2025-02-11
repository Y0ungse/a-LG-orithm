from collections import deque

def solution(priorities, location):
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])  # (우선순위, 원래 위치)
    execution_order = 0  # 실행 순서

    while queue:
        current = queue.popleft()  # 현재 프로세스 꺼내기

        # 큐 안에 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인
        if any(current[0] < process[0] for process in queue):
            queue.append(current)  # 우선순위가 더 높은 프로세스가 있으면 다시 큐에 추가
        else:
            execution_order += 1  # 실행됨 (순서 증가)
            if current[1] == location:  # 목표 프로세스가 실행되었는지 확인
                return execution_order  # 실행된 순서 반환

    return -1  # 예외적으로 실행되지 않는 경우 (실제로 발생할 가능성 없음)
