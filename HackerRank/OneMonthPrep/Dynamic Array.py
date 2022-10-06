def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    
    for q in queries:
        qtype, x, y = q[0], q[1], q[2]
        idx = (x ^ lastAnswer) % n
        
        if qtype == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    
    return answers
