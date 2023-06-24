l1 = [ 1 ]
l2 = [ 0 , 1 ]
y = 1

print(l1)

for j in range(8) :

    
    l = []
    for i in range(0 , y + 1 ) :
        if i != y :
            l.append(l1[i] + l2[i])
        else :
            l.append(l2[i])

    y += 1
    l1 = l
    l2 = [0]
    l2.extend(l)
    print(l)