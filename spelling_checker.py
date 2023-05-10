from textblob import TextBlob
t = 1

while t:
    a = input("Enter the word to be checked") #incorrect spelling
    print("original text:"+str(a)) # printing the original text
    
    b = TextBlob(a) # correcting the text
    # then correct the spelling 
    print("corrected text:"+str(b.correct()))
    t = int(input("Try Agian ? 1 :0 "))
    