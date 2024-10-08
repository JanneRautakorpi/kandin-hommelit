import argparse
from math import log2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", type=str, help="Password to be checked.", required=True)
    parser.add_argument("--length", type=int, help="Required length for password.", required=False)
    parser.add_argument("--charset", type=int, help="Character space", required=False)

    args = parser.parse_args()
    
    passwd = args.password
    length = len(passwd)
    
    reqLength = args.length
    charSpace = args.charset

    entropy = calculateEntropy(reqLength, charSpace) # approx. 104 bits

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
    Calculates entropy. Bigger == better

        Parameters:
            L (int): the required length for the password
            R (int): possible characters
        
        Returns:
            E (float): entropy in bits.
    '''

    E = log2(R**L)
    return E

if __name__=='__main__':
    main()
