names = open("names.txt", "r", encoding="utf8")
for lines in names:
    sep_list = lines.split(",")
sep_list.sort()   # task 1.1
print(sep_list)

without_quotes = []
for quotes in sep_list:  # removing quotes
    if '"' in quotes:
        quotes = quotes[1:-1]
        without_quotes.append(quotes)


alphabet = dict(enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1))  # "1": A
alphabet = dict(zip(alphabet.values(), alphabet.keys()))  # "A": 1

sumList = []
for i in without_quotes:
    counter = 0
    for j in i:
        counter += alphabet[j]
    sumList.append(counter)
print(sumList)  # task 1.2

multiplication = 0
multiList = []
for i in range(1, len(sep_list) + 1):
    multiplication = i * sumList[i - 1]
    multiList.append(multiplication)
print(multiList)  # task 1.3

sumMultiList = sum(multiList)  # task 1.4

print(sumMultiList)  # task 1.5
