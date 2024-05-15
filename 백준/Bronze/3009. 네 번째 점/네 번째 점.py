p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))

p_xs = [p1[0],p2[0],p3[0]]
p_ys = [p1[1],p2[1],p3[1]]

x = None
for xs in p_xs:
    if p_xs.count(xs) == 1:
        x = xs
        break
        
y = None
for ys in p_ys:
    if p_ys.count(ys) == 1:
        y = ys
        break

print(x, y)