def validUTF8(data):
    binaryArr = []
    for a in data:
        binaryArr.append(bin(a)[2:])
    for b in range(len(binaryArr)):
        count = 0
        if len(binaryArr[b]) > 8:
            return False
        binaryArr[b] = '0' * (8 - len(binaryArr[b])) + binaryArr[b]
        if binaryArr[b][0] == '0':
            continue
        elif binaryArr[b][:3] == '110':
            count = 1
        elif binaryArr[b][:4] == '1110':
            count = 2
        elif binaryArr[b][:5] == '11110':
            count = 3
        else:
            return False
        for i in range(count):
            b += 1
            if binaryArr[b][:2] != '10':
                return False
    return True
