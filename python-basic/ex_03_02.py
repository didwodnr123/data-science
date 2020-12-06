sh = input('enter how long did you work? ')
sr = input('enter rate for hour ')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter number.")
    quit()
if fh > 40:
    print('Overtime')
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5) # over time pay
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr

print("pay:", xp)
