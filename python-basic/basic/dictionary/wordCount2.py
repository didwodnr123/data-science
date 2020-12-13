fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1
        # print(word, di[word])

# print(di)

# now we want to find the most common word
largest = -1
theword = None
for key, value in di.items():
    # print(key, value)
    if value > largest :
        largest = value
        theword = key

print('Done', theword, largest)
