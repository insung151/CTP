# HW1 Exercise 5

def frequency_sort(lst):
    # 단어별 빈도수를 저장할 dctionary
    freq_dict = {}

    for key in lst:

        #  아직 빈도수가 저장되지 않은 단어일때
        if not key in freq_dict:
            # 빈도수를 저장할 변수 cnt 초기화
            cnt = 0

            for ele in lst:
                # key를 포함하는 원소가 있을때마다 cnt 1씩 증가
                if key == ele:
                    cnt += 1

            freq_dict[key] = cnt

    # freq_dict의 item들을 리스트로 저장
    l = freq_dict.items()

    # 빈도수가 큰순으로 정렬
    l = sorted(l, key=lambda x: x[1], reverse=True)

    # 빈도수가 같은 것들은 가나다 순으로 정렬
    i = 0
    while i < len(l):
        j = i
        while j+1 < len(l) and l[j][1] == l[j+1][1]:
            j += 1
        l[i:j+1] = sorted(l[i:j+1], key=lambda x: x[0])
        i = j + 1

    l = list(map(lambda x : x[0], l))
    return l


# test example; should be erased before submitting.
# print(frequency_sort(['컴퓨터', '과학', '컴퓨터과학적', '사고', '컴퓨터', '과학', '과학', '사고']))
# print(frequency_sort(['컴퓨터','과학','사고','컴퓨터과학적','가', '가나','나라']))
