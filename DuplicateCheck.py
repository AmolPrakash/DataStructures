'''
given array  find if it duplicates
'''

def check(a):
    for i in range(len(a)):
        if a[abs(a[i])] < 0:
            return True
        a[abs(a[i])] = -a[abs(a[i])]


a = [1,2,2,3,5,6]
b= []
print(check(a))
print (check(b))
        
