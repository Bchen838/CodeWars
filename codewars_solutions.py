# Solution for Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# Solution for Convert a Number to a String 
def number_to_string(num):
    return str(num)
    

# Solution for Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Solution for Vowel Count 
def getCount(sentence): 
    count = 0
    for char in sentence:
        if char in "aeiouAEIOU":
            count = count + 1
    return count