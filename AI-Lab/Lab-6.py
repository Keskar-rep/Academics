# Crypt-Arithmetic Problem

import itertools

# Function to return numerical value of the word

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

# Function to solve the Crypt-Arithmetic Equation

def solve(equation):
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping:{})".format(get_value(right, sol), sol))
    
if __name__ == '__main__':
    equation = input("Enter the cryptarithmetic equation : ")
    solve(equation)