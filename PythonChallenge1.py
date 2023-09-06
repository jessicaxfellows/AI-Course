#Challenge 1
def my_fib(n):
    a = 0
    b = 1
    series = []
    while(a <= n):
        series.append(a)
        a, b = b, a + b
    return series

n = 100
fib_series = my_fib(n)
print(fib_series)

#challenge #2
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
    
num = 5
print("The factorial of", num, "is", factorial(num))

#Challenge 3
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = "Nami is a bear!"
result = count_vowels(input_string)
print("Number of vowels:", result)    

#Challenge 4
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max

list1 = [1, 2 , 3, 4, 5]
print("Max number is:", myMax(list1))

#Challenge 5
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])

string = "The quick brown fox jumps over the lazy dog"
if(check(string) == True):
    print("Pangram")
else:
    print("Not Pangram")

#Challenge 6
def reverse_words(string):
    words = string.split()
    reversed_string = ''
    for i in range(len(words)-1, -1, -1):
        reversed_string += words[i] + ' '
    return reversed_string.strip()

string = "Jess loves Nami bear Jp"    
reversed_string = reverse_words(string)
print(reversed_string)

#Challenge 7
from collections import Counter
def letter_count(string):
    letters = Counter(string)
    for i in string:
        if letters[i] == 1:
            return i
    return None
    
print(letter_count("hheello"))

#Challenge 8
def sorting(list):
    list2 = sorted(list, key=len)
    return list2

list = ["Jessica", "Jp", "Jack", "Evann"]
print(sorting(list))

#Challenge 9
def find_second(list):
    list.sort()
    print("Second smallest number is: ", list[1])

list = [1, 2, 3, 4, 5, 6]
find_second(list)

#Challenge 10
def anagrams(string1, string2):
    string3 = sorted(string1)
    string4 = sorted(string2)
    if string3 == string4:
        print("Anagram")
    else:
        print("Not anagram")

string1 = "Jess"
string2 = "Nami"
anagrams(string1, string2)
    