# run with python3 run_hashcat.py 
# change hash_file and wordlist to your

import subprocess
import time

def run_hashcat(hash_type, hash_file, wordlist, timeout):
    try:
        result = subprocess.run(
            ["hashcat", "-m", str(hash_type), "-a", "0", "-r", "extended-leet.rule", hash_file, wordlist],
            timeout=timeout
        )
    except subprocess.TimeoutExpired:
        print("Hashcat timed out, moving to the next hash.")
        return None  # Something unexpected happened :D

hash_file = "hashlist.hash"
wordlist = "passlist.txt"
timeout = 90  # seconds
hash_type = 0  # md5

with open(hash_file, "r") as f:
    for line in f:
        hash_to_crack = line.strip()
        run_hashcat(hash_type, hash_to_crack, wordlist, timeout)

