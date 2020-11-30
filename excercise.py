"""
1. Define a function sum() and a function multiply() that sums and multiplies (respectively)
 all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and
 multiply([1, 2, 3, 4]) should return 24.
"""


def total(array):
    tot = 0
    for item in array:
        tot += item

    return tot


def multiply(array):
    tot = 1
    for item in array:
        tot *= item

    return tot


"""
2. Define a function caesar_cipher that takes string and key(number), which returns encrypted string
"""


def caesar_cipher(text, cipher_key):
    decoded = ""
    for letter in text:
        letter_index = ord(letter) + cipher_key
        if not letter.isalpha():
            new_letter = letter
        elif letter_index > 122:
            new_letter = chr(letter_index-26)
        else:
            new_letter = chr(letter_index)
        decoded += new_letter

    return decoded


"""
3. Write a function char_freq() that takes a string and builds a frequency listing of the characters
 contained in it. Represent the frequency listing as a Python dictionary. Try it with something like 
 char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def char_freq(text):
    uniques = set(text)
    uniq_dict = dict.fromkeys(uniques, 0)
    for letter in text:
        if letter in uniq_dict:
            uniq_dict[letter] += 1

    return uniq_dict


"""
4. Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") 
should return the string "gnitset ma I".
"""


def reverse(text):
    reversed_list = []
    for letter in text:
        reversed_list.insert(0, letter)
    reversed_text = "".join(reversed_list)
    return reversed_text


"""
5. Define a function, which takes a string with N opening brackets
("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it
consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""


def parenthesized(parenthesis_string):
    result = remove_parenthesis(parenthesis_string)
    if result:
        return "NOT OK"
    else:
        return "OK"


def remove_parenthesis(parenthesis_string):
    substring = "[]"
    clean_up_string = parenthesis_string.replace(substring, "")
    if substring in clean_up_string:
        return remove_parenthesis(clean_up_string)
    else:
        return clean_up_string


"""
6. Create structure for department:
 a) There are 3 types of employee: developer, designer and manager
 b) Each employee has: first name, second name, salary, experiance (years) and manager
 c) Each designer has effectivness coefficient(0-1)
 d) Each manager has team of developers and designers.
 e) Department should have list of managers(which have their own teams)
 f) Department should be able to give salary (for each employee
 message: "@firstName@ @secondName@: got salary: @salaryValue@")
 g) Each employee gets the salary, defined in field Salary.
 If experiance of employee is > 2 years, he gets bonus + 200$,
 if experiance is > 5 years, he gets salary*1.2 + bonus 500
 h) Each designer gets the salary = salary*effCoeff
 i) Each manager gets salary +
   ii) 200$ if his team has >5 members
   iii) 300$ if his team has >10 members
   iiii) salary*1.1 if more than half of team members are developers.
 j) Redefine string representation for employee as follows:
"@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"
"""