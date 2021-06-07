f = open('yesterday.txt', 'r')
yesterday_lyric = ''

while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + '\n'

f.close()
print(yesterday_lyric)

n_of_yesterday = yesterday_lyric.upper().count('YESTERDAY')
print('Number of a word "Yesterday"', n_of_yesterday)