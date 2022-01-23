def get_function_from_string(s):
    mx =0
    intrs = 0
    mn = 0
    words = s.split()
    key = [("maximize","maximum","revenue","max"), ("minimize","minimum","revenue","min"), ("interest","rate", "principal")]
   
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
        return "Maximize Revenue"
    elif max(li)== mn:
        return "Minimize Revenue"
    elif max(li)== intrs:
        return "Interest"
