values = [i.strip().split(" -> ") for i in open("input.txt", "r")]


processed = []

for entry in values:
    start, end = entry  
    
    new_start = start.split(",")
    new_end = end.split(",")
    
    point1 = (int(new_start[0]), int(new_start[1]))
    point2 = (int(new_end[0]), int(new_end[1]))

    processed.append((point1,point2))

positions = dict()

for start, end in processed:
    x1, y1 = start
    x2, y2 = end
    
    if x1 == x2:
        if y2 > y1:
            larger = y2
            smaller = y1
        else:
            larger = y1
            smaller = y2
        
        
        for i in range(smaller, larger+1):
            idx = str(x1)+","+str(i)
            if idx not in positions:
                positions[idx] = 0
            positions[idx] += 1
    elif y1 == y2:
        if x2 > x1:
            larger = x2
            smaller = x1
        else:
            larger = x1
            smaller = x2
        
        for i in range(smaller, larger+1):
            idx = str(i)+","+str(y1)
            if idx not in positions:
                positions[idx] = 0
            positions[idx] += 1
count = 0

for entry in positions:
    if positions[entry] > 1:
        count += 1
     
print(count)
positions2 = dict()
for start, end in processed:
    x1, y1 = start
    x2, y2 = end
    
    delx = (x2 - x1) 
    dely = (y2 - y1)     

    
    if delx == 0:
        x_step = 0
        y_step = (y2 - y1)//abs(y2-y1)
    elif dely == 0:
        y_step = 0
        x_step = (x2 - x1)//abs(x2-x1)
    else:
        y_step = (y2 - y1)//abs(y2-y1)
        x_step = (x2 - x1)//abs(x2-x1)
    
    
    y = y1
    x = x1
    
    while 1:

        idx = str(x)+","+str(y)
        if idx not in positions2:
            positions2[idx] = 0
        positions2[idx] += 1
        if y == y2 and x  == x2:
            break
        y += y_step
        x += x_step
    
count = 0

for entry in positions2:
    if positions2[entry] > 1:
        count += 1
     
print(count)