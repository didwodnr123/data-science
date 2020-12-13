fh = open('mbox-short.txt')
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())


s1 ='Connect Foundation!'
print(len(s1))
s2 = 'Connect\nFoundation!'
print(len(s2))
