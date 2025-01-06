""" participant : 마라톤에 참여한 선수 (List)
    completion : 마라톤을 완주한 선수 (List)
    return : 마라톤을 완주하지 못한 선수 (str) """

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

