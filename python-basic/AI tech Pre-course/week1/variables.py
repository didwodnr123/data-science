color = ['red', 'blue']
color.append('green')
color.insert(0, 'orange')
print(color)

color.remove('blue')
print(color)

del color[0]
print(color)

# packing & unpacking
t = [1,2,3]
a,b,c = t # unpacking
print(t,a,b,c)
