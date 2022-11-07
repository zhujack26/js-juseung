N = int(input())
count = 0
for h in range(N):
    flag = True
    string = list(input())
    if len(string) > 2:  # 4
        for i in range(len(string)-2):  # 0, 1    0,1,2,3
            if not flag:
                break
            for j in range(i+1, len(string)-1): #1 2 3,    # 034    5일떄   #abcda
                for k in range(j+1, len(string)):
                    if string[i] != string[j] and string[j] != string[k] and string[i] == string[k]:
                        count += 1
                        flag= False
                        break
                break
print(N-count)

'''
<<solution2>>

def cnt(s):
    global count
    if len(s) > 2:  # 4
        for i in range(len(s)-2):  # 0, 1    0,1,2,3
            for j in range(i+1, len(s)-1): #1 2 3,    # 034    5일떄   #abcda
                for k in range(j+1, len(s)):
                    if s[i] != s[j] and s[j] != s[k] and s[i] == s[k]:
                        count += 1
                        return
N = int(input())
count = 0
for i in range(N):
    string = list(input())
    cnt(string)
print(N-count)
'''
'''
<<solution 3>>

N=int(input())
count=N
for _ in range(N):
    A=input()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            continue
        elif A[i] in A[i+1:]:
            count-=1
            break
print(count)
'''