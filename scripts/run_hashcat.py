# run with python3 run_hashcat.py 
# change hash_file and wordlist to your

import subprocess
import time

def run_hashcat(hash_type, hash_file, wordlist, timeout):
    """
    Implements timeout feature for Hashcat.

    Args:
        hash_type (bool): Specifies hash type for Hashcat.
        hash_file (bool): File where hash locates.
        wordlist (_type_): Wordlist to use for dictionary attack.
        timeout (_type_): Timeout in seconds.

    Returns:
        None
    """    
    try:
        result = subprocess.run(
            ["hashcat", "-m", str(hash_type), "-a", "0", "-r", "extended-leet.rule", hash_file, wordlist],
            timeout=timeout
        )
    except subprocess.TimeoutExpired:
        print("Hashcat timed out, moving to the next hash.")
        return None  # Something unexpected happened :D

hash_file = "100md5salasanat.txt"
wordlist = "passlist.txt"
timeout = 500  # seconds
hash_type = 0  # md5

with open(hash_file, "r") as f:
    for line in f:
        hash_to_crack = line.strip()
        run_hashcat(hash_type, hash_to_crack, wordlist, timeout)

