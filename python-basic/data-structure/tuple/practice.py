fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

tmp = list()
for key, val in di.items():
    newtup = (val, key)
    tmp.append(newtup)

tmp = sorted(tmp, reverse=True)

num = 0
for t in tmp[:10]:
    num+=1
    print('Rank {} : {}'.format(num, t))
