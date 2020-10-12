def reverseVowels(s):
    vowels = ['a','e','i','o','u', 'A', 'E','I','O','U']
    lt = []
    for i in s:
        if i in vowels:
            lt.append(i)
    lt = lt[::-1]
    pos = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = lt[pos]
            pos+=1
    return ''.join(s)
