class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = word.lower() or word.upper()
        if word[:] == word[::-1]:
            print "is_palindrome"
        else:
            print "No"
                
        return None

print(Palindrome.is_palindrome('DeleVeled'))
