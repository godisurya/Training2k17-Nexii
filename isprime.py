num = input("Enter the number: ")
if num > 1:
    for i in range(2,num):
        #checking for factors
        if (num % i) == 0:
            print num,"is not prime"
            break
    else:
        print num,"is a prime number"

else:
    print num,"is not a prime number"
