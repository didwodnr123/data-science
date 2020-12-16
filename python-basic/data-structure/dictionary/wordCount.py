fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        print(w)
        if w in di:
            di[w] = di[w] + 1
            print('**Existing**')
        else:
            di[w] = 1
            print('**NEW**')
        print(di[w])
        print('\n')

print(di)
