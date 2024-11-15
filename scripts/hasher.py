import hashlib

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


def getText(input_filename):
    try:
        with open(input_filename, 'r') as file:
            for line in file:
                #md5Hasher(line.strip())
                sha256hasher(line.strip(), "SHAhashes.txt")
    except FileNotFoundError:
        print(f"Tiedostoa '{input_filename}' ei löytynyt.")
    except IOError:
        print(f"Tiedoston '{input_filename}' lukemisessa tapahtui virhe.")

getText("AllChar.txt")
getText("alphaCaps.txt")
getText("numbers.txt")