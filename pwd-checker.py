import argparse
from math import log2

'''
For now, we will use global constants for character counts. 
TO DO: change it to be asked form the user as an argument.
'''
CAPITAL_LETTERS = 26                                        # Capital letters in English alphabet
LOWER_CASE_LETTERS = 26                                     # Lower case letters in English alphabet
TOTAL_LETTERS = CAPITAL_LETTERS + LOWER_CASE_LETTERS        # self-explanatory :D
NUMBERS = 10                                                # integers from 0 to 9
TOTAL_CHARS = TOTAL_LETTERS + NUMBERS
REQ_LENGTH = 12                                             # required length for the password (used for entropy calcs)

def main():
    print("This script assumes you use:")
    print("- 52 letters (English alphabet in lower and caps)")
    print("- numbers from 0 to 9")
    print()

    parser = argparse.ArgumentParser()
    parser.add_argument("password", type=str, help="Password to be checked.")
    args = parser.parse_args()
    
    passwd = args.password
    length = len(passwd)
    entropy = calculateEntropy(REQ_LENGTH, TOTAL_CHARS)
    print(entropy)
    containsNumber = containNumber(passwd)
    containsLowerCase = containLowerCase(passwd)
    containsCapital = containCapital(passwd)



def containCapital(password):
    return any(i.isupper() for i in password)

def containNumber(password):
    return any(i.isdigit() for i in password)

def containLowerCase(password):
    return any(c.islower() for c in password)

def calculateEntropy(L, R):
    '''
    Calculates entropy.

        Parameters:
            L (int): the required length for the password
            R (int): possible characters
    '''

    E = log2(R**L)
    return E

if __name__=='__main__':
    main()
