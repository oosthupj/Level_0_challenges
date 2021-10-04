def common_characters(string1, string2):
    result ="Common letters: None"
    for letters in string1.lower():
        if letters in string2.lower():
            if result =="Common letters: None":
                result="Common letters: " + letters
            else:
                result=result + "," + letters
    return result

'''
This is just to test the function
'''
print(common_characters('house','computers'))
print(common_characters('Ear','Dear'))
print(common_characters('EAR','DEAR'))