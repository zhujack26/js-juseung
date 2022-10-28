# for tc in range(1, int(input())+1):
#     string = list(input())
#     stack = []
#     result = 0
#     for i in string:
#         if i == '{' or i == '}' or i == '(' or i == ')':
#             stack.append(i)
#             for j in range(1, len(stack)):
#                 if stack[j-1] == '{' and stack[j] == '}' :
#                     stack.pop(j)
#                     stack.pop(j-1)
#                 elif stack[j-1] == '(' and stack[j] == ')' :
#                     stack.pop(j)
#                     stack.pop(j-1)
#     if len(stack) == 0:
#         result = 1
#     print(f'#{tc}', result)

T = int(input())
for tc in range(1, 1 + T):
    arrs = list(input())
    lst = []
    op = ["{", "("]
    result = 1
    for idx in range(len(arrs)):
        if len(lst) == 0 and arrs[idx] == "}" :
            result = 0
            break
        elif len(lst) == 0 and arrs[idx] == ")" :
            result = 0
            break

        elif arrs[idx] in op:
            lst.append(arrs[idx])

        elif len(lst) !=0 and arrs[idx] == "}" and lst[-1] == "{":
            lst.pop()

        elif len(lst) !=0 and arrs[idx] == ")" and lst[-1] =="(":
            lst.pop()

    if len(lst) !=  0:
        result = 0

    elif "{" not in arrs and "(" not in arrs and ")" not in arrs and "}" not in arrs:
        result = 0

    print(f'#{tc} {result}')