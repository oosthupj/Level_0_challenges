def common_characters(string1, string2):
    vowels = "aeiouAEIOU"
    result ="Common letters: None"
    for letters in string1:
        if letters in string2:
            if result =="Common letters: None":
                result="Common letters: " + letters
            else:
                result=result + "," + letters
    print(result)

common_characters('house','computers')
