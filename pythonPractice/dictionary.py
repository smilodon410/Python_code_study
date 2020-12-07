# Dictionary 를 활용한 Count
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

# Dictionary : get 함수
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# 문장에서 가장 많이 나온 단어 찾기
# count = dict()
# print('Enter a line of text: ')
# line = input('')
# print('')
#
# words = line.split()
#
# print('Words: ', words)
#
# print('Counting...')
# for word in words:
#     count[word] = count.get(word, 0) + 1
# print('Count', count)

# 파일에서 제일 많이 나온 단어와 횟수 출력하기
# name = input('Enter File Name: ')
# handle = open(name)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)

# Dictionary 를 활용한 데이터 빈도수 측정
fname = input('Enter File: ')
# if len(fname) < 1:
#     fname = 'intro.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # oldcount = di.get(w,0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount          # 과정
        di[w] = di.get(w, 0) + 1
print('I am working...')
# Find the most common word
largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k
print('Done!', 'Counts:', largest, 'Word:', theword)