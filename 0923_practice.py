def preorder(n):
    global count
    if n == 0:
        return
    count += 1
    preorder(ch1[n])
    pre