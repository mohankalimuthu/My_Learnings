#https://www.geeksforgeeks.org/problems/sandwiched-vowels5158/1?page=4&category=Arrays&difficulty=Basic&sortBy=submissions

'''
concept explanation:
remove vowel from sandwiched:
that means->:
    1. the character must be VOWEL
    2. the character must have a consonant before and after it
    3. both consonant must be immediately adjacent

what are valid/ invalid?
    Remove
        "bab" → remove a
        "ten" → remove e
        "dog" → remove o

    Keep (not sandwiched)
        At the string beginning
            "a..." → no left consonant
        At the string end
            "....a" → no right consonant
        Vowel followed by vowel
            "ae" → not sandwiched
        Vowel preceded by vowel
            "ea" → not sandwiched
'''
'''
1. initialize the result variable as 'res', it's stored new characters.
2. create a list it contain vowel alphabetical words
3. iterate through the len(input string)
    if condition: string of fast letter and last letter must ignord in
            if condition: previous character must not be a vowel and current character must be a vowel and next character must not be a vowel.
                            remove the character, instead of remove we simply ignore by the 'continue'.
            else:
             store the other characters to res variable
    else:
        store that ignored character to res variable.
'''



def sandwhich(s):
    res = ''
    vowel = ['a','e','i','o','u']
    for i in range(len(s)):
        if i!=0 and i!=len(s)-1:
            if s[i-1] not in vowel and s[i] in vowel and s[i+1] not in vowel:
                continue
            else:
                res+=s[i]
        else:
            res+=s[i]
    return res

s = "bab"
print(sandwhich(s))