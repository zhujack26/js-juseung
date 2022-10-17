flag = True
n = int(input())
for h in range(n):
    string = list(input())
    count = []
    for i in range(len(string)):
        if flag == False:
            break
        for j in range(len(string)-1):
            if 0<= i+j+1 <len(string) and string[i] != string[i+j]:
                if string[i] == string[i+j+1]:
                    count.append(1)
                    flag = False
                    break
    print(sum(count))
