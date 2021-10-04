def get_vowels(word):
    vowels = "aeiouAEIOU"
    number_of_vowels = 0
   
    for letters in word:
        if letters in vowels:
            if number_of_vowels == 0:
                result=letters
                number_of_vowels +=1
            else:
                if letters.lower() not in result.lower():
                    result=result + ", " + letters

    if number_of_vowels == 0:
        print("Vowels: None")
    else:
            print("Vowels: "+ result.lower())

'''
This is just to test the function
'''
get_vowels("Umuzi")
get_vowels("JacoO")