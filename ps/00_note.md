## round 함수

- 파이썬의 round 함수는 오사오입 방식이다. 즉, 0.5 이상이 아닌, 0.5 초과여야 올림을 수행하는 방식이다. 따라서 우리가 알고 있는 반올림을 구현하기 위해서는 round될 값에 아주 작은 수를 더해주자. 0.000001이라던가...

- 참고 문제: [백준 18110번](https://www.acmicpc.net/problem/18110)
- 정답 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    exit(0)
cut = round(N * 0.15 + 0.0000001)
score = []
for _ in range(N):
    score.append(int(input()))

score.sort()
score = score[cut:N-cut]
print(round((sum(score) / (N - cut*2)) + 0.0000001))
```
