import argparse
from math import log2

def main():
    print("This script assumes you use:")
    print("- 26 letters (English alphabet)")
    print("- numbers from 0 to 9")
    print()

    parser = argparse.ArgumentParser()
    parser.add_argument("password", type=str, help="Password to be checked.")
    args = parser.parse_args()
    
    passwd = args.password
    length = len(passwd)
    

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
