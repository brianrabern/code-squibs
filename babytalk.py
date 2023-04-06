def baby_talk(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    junk = []
    for t in substrings:
        first, second = t[:len(t)//2], t[len(t)//2:]
        if first == second:
            junk.append(first)
    m = 0
    for j in junk:
        if len(j) > m:
            m = len(j)
    return m*2







x = 'BABAGOOGOOGOOGOOGOOGOOBA'

print(baby_talk(x))
