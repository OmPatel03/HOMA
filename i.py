def functionType(s):
    mx =0
    intrs = 0
    mn = 0
    words = s.split()
    key = {("maximize","maximum","revenue"):"Maximum Revenue",("minimize","minimum","revenue"):"Minimum Revenue",("interest","rate", "principal"):"Interest"}
   
    for a in key[0]:
        if a in words:
            mx=mx+1
    for n in key[1]:
        if n in words:
            mn = mn+1
    for i in key[2]:
        if i in words:
            intrs+=1
    li = (mx,mn,intrs)
    if max(li) == 0:
        return "This Type of function cannot be evaluated yet"
    elif max(li) == mx:
        return "Maximum Revenue"
    elif max(li)== mn:
        return "Minimum Revenue"
    elif max(li)== intrs:
        return "Interest"
print(functionType("minimum the revenue if for every 1 dollar i add to the flowers price then 1 fewer people buy it. 25 people originally by the flowers and the flowers cost 10 dollars"))

def maxRev(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for c in punctuations:
        s = s.replace(c,"")
    segements = []
    word = s.split()
    x = 0
    while word != []:
        l =[]
        try:
            int(word[x])
            for y in range(x):
                l.append(word[y])
            segements.append((l,word[x]))
            del(word[0:y+2])
            x=0
        except ValueError:
            x=x+1
            pass
    segements 
    return segements

def minRev(s):
    return 0

def interest(s):
    return 0