""" participant : 마라톤에 참여한 선수 (List)
    completion : 마라톤을 완주한 선수 (List)
    return : 마라톤을 완주하지 못한 선수 (str) """

import collections

def solution(participant, completion):
    ## 참가자 명단에서 완주자 명단을 빼기
    answer = collections.Counter(participant) - collections.Counter(completion)
    answer = list(answer.keys())[0]
    return answer 

