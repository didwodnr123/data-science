fname = input('Enter the file namee: ')
try:
    fhand = open(fname)
except:
    print('File cannot be oppend:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject') :
        count = count + 1
print('There were', count, 'subject lines in', fname) 
