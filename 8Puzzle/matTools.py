#These functions are for formatting
#flatten array
def flatten(arry):
    return [num for row in arry for num in row]

#convert string space to 0
def oSpce(lst):
    return [0 if i==" " else i for i in lst]

#makes string of numbers
def dence(lst):
    return ''.join(map(str,lst))

#combine the formatting functions
def reMat(arryLst):
    out = []
    for arry in arryLst:
        arry = flatten(arry)
        arry = oSpce(arry)
        arry = dence(arry)
        out.append(arry)
    return out
