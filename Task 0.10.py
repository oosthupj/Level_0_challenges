def common_characters(string1, string2):
    #vowels = "aeiouAEIOU"
    result ="Common letters: None"
    for letters in string1.lower():
        if letters in string2.lower():
            if result =="Common letters: None":
                result="Common letters: " + letters
            else:
                result=result + "," + letters
    print(result)

common_characters('house','computers')
common_characters('Ear','Dear')