"""
# Problem 2:
print "----------------------Problem 2-----------------------"
def factorial(x):
     if x == 0:
         return 1
     else:
         return x * factorial(x-1)
a=raw_input("Please enter  a number:")
b =int(a)
print "The Factorial for the number enterd is: ", factorial(b)

print
print
#Problem 2:
print "---------------Problem 3-----------------"
print
n = int(raw_input("Please Enter a number here: "))

#Problem 3:
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
print "The fibonacci of the Number entered is:", map(fibonacci, range(0, n))

print
print


def prime():



    a =raw_input("Please Enter a Number:")
    n=int(a)

    print "This is :"
    prime_count = 0
    possible_prime = 2
    while prime_count < n:
        divisor_count = 0
    
        for i in range(1,possible_prime+1):

       
            if possible_prime % i == 0:
            
                divisor_count += 1

 
        if divisor_count == 2:
       
            #print possible_prime,
            return True
       
            prime_count += 1
    
        
            if prime_count % 10 == 0:
           
                return False

        
        possible_prime += 1

print prime()

"""
def isPalindrome(strin):
    #strin= raw_input ("Please enter a frase:")
    newstring= strin[::-1]
    if newstring==strin:

        print "This is a Palindrome"
        
        
    else:
        print "This is not a palindrome"
    print "This is your origional Text: ", strin
    print "This is your new text: ", newstring
    return True
strin= raw_input ("Please enter a frase:")
print isPalindrome(strin)
