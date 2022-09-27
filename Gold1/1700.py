import sys

input = sys.stdin.readline


n, k = map(int, input().split())
order = list(map(int, input().split()))

plugs = []
answer = 0

for idx, item in enumerate(order):
    if item in plugs:
        continue

    elif len(plugs) < n:
        plugs.append(item)
        

    t
    else:
        for p in plugs:
            if p not in order[idx:]:


print(answer)
