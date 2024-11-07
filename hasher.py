import hashlib


def md5Hasher(text, output_filename="hashes.txt"):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    md5_hash = md5.hexdigest()
    with open(output_filename, 'a') as file:
        file.write(md5_hash + '\n')
    
    #print(f"MD5-tiiviste '{md5_hash}' tallennettu tiedostoon '{output_filename}'.")

def getText(input_filename):
    try:
        with open(input_filename, 'r') as file:
            for line in file:
                md5Hasher(line.strip())
    except FileNotFoundError:
        print(f"Tiedostoa '{input_filename}' ei löytynyt.")
    except IOError:
        print(f"Tiedoston '{input_filename}' lukemisessa tapahtui virhe.")

getText("numbers.txt")
