import hashlib
import os 
import whirlpool
import bcrypt

def sha256hasher(data, outfile=None):
    """
    Creates a SHA3-256 hash for given data.

    Args:
        data str: string to hash
        outfile (.txt preferably): where to output hash(es). Defaults to None.
    """    
    updateData = data.encode('utf-8')
    hash_obj = hashlib.sha3_256()
    hash_obj.update(updateData)
    hexHash = hash_obj.hexdigest()
    try:
        with open(outfile, 'a') as file:
            outfile.write(hexHash + '\n')
    except IOError:
        print(f"Tiedoston lukemisessa tapahtui virhe.")

def md5Hasher(text, output_filename=None):
    """
    Creates MD5 hash.

    Args:
        text str: string to hash.
        output_filename (.txt, optional): output file for hash(es). Defaults to None.
    """    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    md5_hash = md5.hexdigest()
    with open(output_filename, 'a') as file:
        file.write(md5_hash + '\n')

def whirlpooler(input):
    """
    Uses Whirlpool hash algorithm to hash passwords.

    Args:
        input (str): string to be hashes
    """    
    
    string = input.encode('utf-8')
    wp = whirlpool.new(string)
    hash = wp.hexdigest()

    with open("whirlpool.hash", "a") as file:
        file.write(hash + "\n")

def bcrypter(input):
    string = input.encode('utf-8')
    rounds = 10

    salt = bcrypt.gensalt(rounds=rounds)
    hash = bcrypt.hashpw(string, salt)
    hashedPassword = hash.decode('utf-8')
    #print(hashedPassword)
    with open("bcrypt.hash", "a") as file:
        file.write(hashedPassword + "\n")


def getText(input_filename):
    """
    Goes through password list and then hashes each password.

    Args:
        input_filename (str): password list to take passwords from
    """    
    try:
        with open(input_filename, 'r') as file:
            for line in file:
                #md5Hasher(line.strip())
                #sha256hasher(line.strip(), "SHAhashes.txt")
                #whirlpooler(line.strip())
                bcrypter(line.strip())

    except FileNotFoundError:
        print(f"Tiedostoa '{input_filename}' ei löytynyt.")
    except IOError:
        print(f"Tiedoston '{input_filename}' lukemisessa tapahtui virhe.")


#getText("AllChar.txt")
#etText("alphaCaps.txt")
#getText("numbers.txt")

current_dir = os.path.dirname(os.path.abspath(__file__))
ordlista = os.path.join(current_dir, "../datasets/ordlista.txt")

getText(ordlista)
