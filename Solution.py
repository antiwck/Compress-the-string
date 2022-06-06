def solve(s):
    vowels = {'a','e','i','o','u'}
     # Capitalize first letter
    res = "" + s[0].upper()
    ctr = 0
    for i in range(1, len(s)):
        # To append non-vowels amount once vowel is read and reset counter
        if s[i] in vowels and ctr != 0:
            res+=str(ctr)
            ctr=0
        # To append vowel if vowel is read and the latest vowel in result is not the same as current read vowel
        if s[i] in vowels and res[-1] != s[i]:
            res+=s[i]
        # To count consecutive non-vowel amount
        elif s[i] not in vowels:
            ctr+=1
    # To append non-wovel in the end of string if no vowel encounter at the end
    if ctr != 0:
        res+=str(ctr)
    return res

for _ in range(int(input())):
    n=int(input());string=input()
    print(solve(string))
