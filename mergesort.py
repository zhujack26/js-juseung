arr = [69, 10, 30, 2, 16, 8, 31, 22]


def merge_sort(input_list):  # 쪼개는 애

    if len(input_list) == 1:  # 1개 짜리라면 더 쪼갤 필요 없으니까
        return input_list  # 그대로 다시 리턴하기

    mid = len(input_list) // 2  # 기준점이 되는 값 (+1 하면 무한루프)
    left_half = input_list[:mid]  # 여기서 아이디값 분리
    right_half = input_list[mid:]  # 오른쪽 반땡

    left = merge_sort(left_half)  # 분할정복 재귀호출
    right = merge_sort(right_half)

    return merge(left, right)  # 이미 아이디값 분리된 애가 인자로! + 쪼개기가 끝내면 결국 끝은 붙이기 로직!


def merge(left, right):  # 합치는 애
    result = [0]*(len(left)+len(right))  # 들어갈 틀
    l = r = idx = 0  # 포인터 3개는 전부 0으로 초기화

    while l < len(left) and r < len(right):  # 여기 and 여야함!
        if left[l] <= right[r]:  # 얘 덕분에 안정 정렬 가능
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    while l < len(left):  # 하나만 돌게될것, 떨거지 처리
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        result[idx] = right[r]
        r += 1
        idx += 1

    return result  # 아이디값 새로 파진걸 리턴해서 안꼬임


print(merge_sort(arr))
# 원본은 안건드림 => id값을 새로 팠으니까
# print(arr)