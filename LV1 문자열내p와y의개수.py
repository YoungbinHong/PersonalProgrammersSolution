def solution(s):
    answer = True
    split = []
    for i in s:
        split.append(i)
    
    num_of_p,num_of_y = 0,0
    
    for i in split:
        if i == 'p' or i == 'P':
            num_of_p += 1
        elif i == 'y' or i == 'Y':
            num_of_y += 1
    
    if num_of_p != num_of_y:
        answer = False

    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))
