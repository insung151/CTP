# HW1 Exercise 6

def count_word_lists(lst, word, k):
    # 조건에 해당하는 리스트가 몇개인지를 담기 위한 변수
    result = 0
    for li in lst:
        # 한개의 리스트 안에 단어가 몇개 있는지를 담기 위한 변수
        cnt = 0
        for ele in li:
            if ele == word:
                cnt += 1

        # 단어가 k개 이상 들어있다면 result에 1개추가
        if k <= cnt :
            result += 1

    return result
# test example; should be erased before submitting.
# lst_example = [['가', '나', '가'], \
# 			  ['가', '나', '나'], \
# 			  ['가', '가', '다']]
# lst = [ ['가', '가가', '가가가'], ['가가', '가가', '가가가'] ]
# print(count_word_lists(lst, '가', 1))
# print(count_word_lists(lst, '가', 2))
# print(count_word_lists(lst, '가가', 1))
