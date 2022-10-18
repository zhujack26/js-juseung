N = int(input())
count = 0
for h in range(N):
    string = list(input())
    if len(string) > 2:  # 4
        for i in range(len(string)-1):  # 0, 1,2
            for j in range(1, len(string)-1): #1,2,
                if 1<= i+j+1 <len(string) and string[i] != string[i+j] and string[i+j] != string[i+j+1] and string[i] == string[i+j+1]:
                    count += 1
                    break
            break
print(N-count)
