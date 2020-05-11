def solution(answers):
    score,supo1,supo2,supo3 = [0,0,0],list(),list(),list()
    for i in range(len(answers)):
        supo1.append(i%5+1)
        #print(supo1)
        if i%2 == 0: supo2.append(2)
        elif i%8 == 1: supo2.append(1)
        elif i%8 == 3: supo2.append(3)
        elif i%8 == 5: supo2.append(4)
        elif i%8 == 7: supo2.append(5)
        #print(supo2)
        if i%10 == 0 or i%10 == 1: supo3.append(3)
        elif i%10 == 2 or i%10 == 3: supo3.append(1)
        elif i%10 == 4 or i%10 == 5: supo3.append(2)
        elif i%10 == 6 or i%10 == 7: supo3.append(4)
        elif i%10 == 8 or i%10 == 9: supo3.append(5)
        #print(supo3)
    for i in range(len(answers)):
        if supo1[i] == answers[i]: score[0] += 1
        if supo2[i] == answers[i]: score[1] += 1
        if supo3[i] == answers[i]: score[2] += 1
    winner = list()
    if max(score[0],score[1],score[2]) == score[0]: winner.append(1)
    if max(score[0],score[1],score[2]) == score[1]: winner.append(2)
    if max(score[0],score[1],score[2]) == score[2]: winner.append(3)
    #for i in range(len(score)):
    #    if score[i] == len(answers): score[i] = '모든'
    #    print(f'수포자 {i+1}은 {score[i]} 문제를 맞혔습니다.')
    return winner

test = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(solution(test))