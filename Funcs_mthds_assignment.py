#Write a function that computes the volume of a sphere given its radius
def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)

#Write a function that checks whether a number is in a given range (inclusive of high & low)
def ran_check(num,low,high):
    #check if the number is between low and high(including low and high)
    if num in range(low, high):
        print "is in the range" %str(num)
    else:
        print "The number is outside the range."

#if you only wanted to return a boolean:

def ran_bool(num,low,high):
    return num in range(low, high)

ran_bool(3,1,9)
True #results

#write a python function that accepts a string and calculate the number of upper case letters and lower case letters


#write a python function that takes a list and returns a new list with unique elements of the first list
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1,2,3,4,5]
def unique-list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

#write a python function to multiply all the numbers in a list
Sample List : [1,2,3,-4]
Expected output: -24

def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total

multiply([1,2,3-4])
-24 #output



#write a python function that checks whether a passed string is palindrome or not
  #palindrome is a word, phrase or sequence
  def palindrome(s):
      return s == s[::-1]

  palindrome('helleh')
  True #results



#write a python function to check whether a string is pangram or not
 #note: pangrams are words or sentences containing every letter of the alphabet at least once
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset= set(alphabet)
    return alphaset <= set(str1.lower())

string.ascii_lowercase






