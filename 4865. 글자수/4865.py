T = int(input())
for tc in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    save = []
    for i in str1:
        save.append(str2.count(i))
    print(f'#{tc} {max(save)}')

