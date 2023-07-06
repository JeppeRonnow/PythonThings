
def enCode(str1, str2):
    res = []

    for i in range(len(str2)):
        index = i % len(str1)
        res.append(chr(ord(str1[index]) + ord(str2[i])))
    
    return ''.join(res)

gem = enCode("abc","oweqweqwe")

print(gem)

def deCode(str1, str2):
    res = []

    for i in range(len(str2)):
        index = i % len(str1)
        res.append(chr(ord(str2[i]) - ord(str1[index])))
    
    return ''.join(res)

print(deCode("abc",gem))