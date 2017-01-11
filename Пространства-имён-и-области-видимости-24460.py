#https://stepik.org/lesson/Пространства-имён-и-области-видимости-24460/step/9

N = int(input())
d = {}
spaces = {}

for i in range(N):
    cmd, a1, a2 = input().split()
    
    if cmd == 'add':
        if a1 not in d:
            d[a1] = set()
            
        
        d[a1].add(a2)
    
    if cmd =='create':
        spaces[a1] = a2

    if cmd == "get":
        s1 = a1
        s2 = a2
        
        if d[s1]:
            GG = d[s1]
        while d[s1]:
            if s2 in d[s1]:
                print(s1)
                break
            else:
                if spaces[s1]:
                    FF = spaces[s1]
                if spaces[s1]:
                    s1 = spaces[s1]
                else:
                    print(None)
                    break
print(spaces)
print(d)
    