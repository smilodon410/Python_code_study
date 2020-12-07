# Collection 을 활용한 빈도수 상위 10개 단어 찾기
fhand = open('intro.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = []
for k,v in counts.items():
    newtp = (v, k)
    lst.append(newtp)

lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k, v)

# 더 짧게
# c = {'a':10, 'b':1, 'c':22}
# print(sorted([(v,k) for k,v in c.items()]))
