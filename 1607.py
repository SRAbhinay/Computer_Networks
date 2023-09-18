def solve(number):
   print("{:.2f}".format(number))

t_capacity = float(input())
n = int(input())

prices = [0] * (n+1)
quantity = [0] * (n+1)
ratio = [0] * (n+1)

arr = []

for i in range(n):
    a, b = map(float, input().split())
    arr.append([a, b])
    ratio[i] = a/b
    prices[i] = a
    quantity[i] = b

for i in range(n):
    for j in range(n):
        if ratio[i] > ratio[j]:
            ratio[i], ratio[j] = ratio[j], ratio[i]
            prices[i], prices[j] = prices[j], prices[i]
            quantity[i], quantity[j] = quantity[j], quantity[i]

total = 0
ans = 0
x = 0

while total < t_capacity and x < n:
    if total + quantity[x] > t_capacity:
        x += 1
    else:
        total += quantity[x]
        ans += prices[x]
        x += 1

t_capacity -= total

if t_capacity != 0:
    ans += ratio[x-1]*t_capacity

solve(ans)
