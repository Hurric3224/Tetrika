ip = open("hits.txt", "r", encoding="utf8")
empty = []
emptyDict = {}
for line in ip:
    empty.extend(line.split())
empty = empty[1::3]  # only ID's
for i in empty:
    emptyDict[i] = emptyDict.get(i, 0) + 1  # numbers of meetings
emptyDict = {v: k for k, v in emptyDict.items()}  # count: ID
listKeys = list(emptyDict.keys())
listKeys.sort(reverse=True)

answer = []
for i in range(5):
    answer.append(emptyDict[listKeys[i]])
print(answer)  # task 2
