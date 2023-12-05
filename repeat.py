from collections import Counter

def duplicate_encode(word):
    #your code here
    from collections import Counter

    not_seen=[]

    for i in word.lower():
        if i not in not_seen:
            not_seen.append(i)

    result=word.lower()
    counter=Counter(word.lower())

    for p in not_seen:
        print(f"{p} {counter[p]}")
        if counter[p] > 1:
            result = result.replace(p,")")
        else:
            result = result.replace(p,"(")
    return result

var = "awopu@Lx!zpYTATuSyjgKoU(R(("
duplicate_encode(var)
