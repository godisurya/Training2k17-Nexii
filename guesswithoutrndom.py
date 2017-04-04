#while True:
for i in range(5):
    a = input("Enter your guess in between 1 to 10: ")
    b = 5
    if a == b:
        print "Wow! Superb, you guessed right"
        break
    elif a > b:
        print "Sorry! Number is Smaller than the guess"
        #print "Guess again"
    else:
        print "Sorry! Number is Higher than the guess"
        #print "Guess again"
    

print "Over"
