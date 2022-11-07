a = [2, 8, 7, 1, 3, 5, 6, 4]

def lomuto(low, high):
    def partition(low, high):
        pivot = a[high]  # 로무토는 맨 오른쪽을 초기 피봇으로 일단 삼는다
        left = low  # 우선 제일 왼쪽은 low 값으로 초기화

        for right in range(low, high):  # right => 이동하는 포인터
            if a[right] < pivot:  # 만약 돌아다니면서 피봇보다 작은걸 구한 경우?
                a[left], a[right] = a[right], a[left]  # left,  right 위치 스왑
                left += 1  # 칸막이 한칸 이동

        a[left], a[high] = a[high], a[left]  # 솎아내는거 다 끝나면 칸막이 위치와 맨 오른쪽 피봇값을 스왑

        return left  # 칸막이 인덱스를 뱉음

    if low < high:
        pivot = partition(low, high)  # 뱉어진 칸막이를 기준으로 반땡
        lomuto(low, pivot-1)
        lomuto(pivot+1, high)

lomuto(0, len(a)-1)
print(a)