for tc in range(1, int(input())+1):
    string = list(input())
    result = 0
    stack = []
    for i in string:
        stack.append(i)
        for j in range(1, len(stack)):
            if stack[j] == stack[j-1]:
                stack.pop(j)
                stack.pop(j-1)
    print(f'#{tc}', len(stack))
