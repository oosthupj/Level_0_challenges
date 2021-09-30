def get_vowels(word):
    vowels = "aeiouAEIOU"
    result ="Vowels: None"
    for letters in word:
        if letters in vowels:
            if result =="Vowels: None":
                result="Vowels: " + letters
            else:
                result=result + "," + letters
    result = result
    print(result.lower())

get_vowels("Umzi")