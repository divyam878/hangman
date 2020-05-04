import time 
name = input("what's your name? ")
print ("Hello " + name , "let's play hangman!!")
print("")


time.sleep(1)
print ("start guessing...")
time.sleep(0.5)
word = "secret"
guesses= ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print (char),
        else:
            print ("_"),
            failed+=1
                
    if failed == 0:
        print("you won")

        break

    print 
    guess = input("guess a character")
    guesses +=guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have " +turns , "guesses left")
        if turns==0:
            print("you lose")



