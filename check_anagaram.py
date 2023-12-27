str1 = 'Care'
str2 = 'Race'
str1 = str1.lower()
str2 = str2.lower()
str1 = sorted(str1)
str2 = sorted(str2)
if str1==str2:
    print('given strings are anagram')
else:
    print('not are anagrams')