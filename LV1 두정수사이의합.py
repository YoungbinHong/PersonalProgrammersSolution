def solution(a, b):
    if a>b:
        a,b = b,a
    
    answer = 0
    num = list(range(a,b+1,1))
    for i in range(len(num)):
        answer += num[i]
    return answer

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))
