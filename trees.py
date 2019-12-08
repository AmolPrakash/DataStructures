'''

TREES

'''
##finding the depth of a tre using 
def  depth(p):
    d  = 0
    for i in range(len(p)):
        count = 1
        while (p[i] != -1):
            count += 1
            i = p[i]
        d = max(count, d)
    return d


## using dictionary 
def  depth2(p):
    dic = {}
    depth  = 0
    for i in range(len(p)):
        count = 1
        while (p[i] != -1):
            if dic[p[i]] != None:
                depth =+ dic[p[i]]
                break 
            else:    
                count += 1
                i = p[i]
        dic[i] = count
        depth = max(count, depth)
    return depth

p = [-1,0,0,0,2,2,5,6,6,8]
print(depth2(p))

    
