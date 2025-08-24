def count_vowel_consonants(m):
    vowels="aeiouAEIOU"
    vcount=0
    con_count=0
    for char in m:
      if char.isalpha():
        if char in vowels:
            vcount+=1
        else:
            con_count+=1
    print(vcount,con_count)        
count_vowel_consonants("Hello world")         
    