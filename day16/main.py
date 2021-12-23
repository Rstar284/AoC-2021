l = [l.strip() for l in open("input").readlines()]
a = l[0]
versionTotal = 0

def parsePacket(enc):
    global versionTotal
    numParsed = 0
    version = int(enc[:3], 2)
    versionTotal+=version
    enc = enc[3:]
    numParsed+=3
    typeid = int(enc[:3], 2)
    enc = enc[3:]
    numParsed+=3
    if typeid == 4:
        curStr = ''
        while True:
            currGroup = enc[:5]
            enc = enc[5:]
            numParsed+=5
            curStr+=currGroup[1:]
            if(currGroup[0] == '0'):
                break
        return enc, numParsed, int(curStr, 2)
    else:
        vals = []
        ltid = enc[0]
        enc = enc[1:]
        numParsed+=1
        if(ltid == '0'):
            nbits = int(enc[:15], 2)
            enc = enc[15:]
            numParsed+=15
            while nbits > 0:
                cur, numParsed2, oval = parsePacket(enc)
                nbits-=numParsed2
                enc = cur
                numParsed+=numParsed2
                vals.append(oval)
        else:
            npackets = int(enc[:11], 2)
            enc = enc[11:]
            numParsed+=11
            for i in range(npackets):
                cur, numParsed2, oval = parsePacket(enc)
                enc = cur
                numParsed+=numParsed2
                vals.append(oval)
        val = 0
        if typeid == 0:
            val = sum(vals)
        elif typeid == 1:
            val = 1
            for i in vals: val*=i
        elif typeid == 2:
            val = min(vals)
        elif typeid == 3:
            val = max(vals)
        elif typeid == 5:
            val = int(vals[0] > vals[1])
        elif typeid == 6:
            val = int(vals[0] < vals[1])
        elif typeid == 7:
            val = int(vals[0] == vals[1])
        return enc, numParsed, val

enc = ''
for i in a:
    b = bin(int(i, 16))[2:]
    while len(b) < 4:
        b = '0'+b
    enc+=b

parsePacket(enc)
print(versionTotal)
print(parsePacket(enc)[2])
