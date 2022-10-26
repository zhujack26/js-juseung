for tc in range(1, int(input())+1):
    string = list(input())
    stack = []
    result = 0
    for i in string:
        if i == '{' or i == '}' or i == '(' or i == ')':
            stack.append(i)
            for j in range(1, len(stack)): # 0이 아니라면, pop 조심
                if stack[j] == '}' and stack[j - 1] == '{':
                    stack.pop(j)
                    stack.pop(j - 1)
                elif stack[j] == ')' and stack[j - 1] == '(':
                    stack.pop(j)
                    stack.pop(j - 1)
    if len(stack) == 0:
        result = 1
    print(f'#{tc}', result)