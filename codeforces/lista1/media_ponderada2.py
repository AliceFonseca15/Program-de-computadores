v1, v2 = map(int,input().split())
b, p = map(int,input().split())
media = (v1 * b + v2 * p) // (b + p)
print(media)