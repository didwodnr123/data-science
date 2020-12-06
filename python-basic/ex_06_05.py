str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(":")
print(ipos)
piece = str[ipos+2:]
print(piece)
value = float(piece)
print(value)

words = 'Hello world'
pos = words.find(' ')
print(pos)
print(words[:pos])
