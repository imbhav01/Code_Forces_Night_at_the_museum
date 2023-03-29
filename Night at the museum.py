z = str(input())
t = 0
prev = ord('a')
for i in z:
        diff=abs(ord(i)-prev)
        
        if diff>13:
            t+=26-diff
        else:
            t+=diff
        prev=ord(i)

print(t)