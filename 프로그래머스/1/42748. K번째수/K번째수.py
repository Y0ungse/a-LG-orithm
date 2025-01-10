def solution(array, commands):
    answer = []
    
    #answer [1, 5, 2, 6, 3, 7, 4]
    #commands [i, j, k] -> [2, 5, 3] didi
    for i in commands:
        
        ary = array[i[0]-1: i[1]] # i[0]-1 ~ i[1]-1
        ary.sort()  
        answer.append(ary[i[2]-1]) # i[2]-1  
    return answer