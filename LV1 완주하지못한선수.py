def solution(participant, completion):
    participant.sort()
    completion.sort()
    size_of_completion = len(completion)

    for i in range (size_of_completion):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko",
"filipa"],["marina", "josipa", "nikola", "vinko", "filipa"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
