n = int(input())  # 1~1000까지의 수 입력
if n > 1000:
    print("1000이하의 수를 입력하세요")
    n = int(input())

two_xn = [0, 1, 2]
for i in range(3, n+1):
    two_xn.append(two_xn[i-2]+two_xn[i-1])
print(two_xn[n] % 10007)
