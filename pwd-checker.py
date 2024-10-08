import argparse
from math import log2

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
    entropy = calculateEntropy(8, (26 + 26 + 10 + 32))
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
