**brute force**\
Tässä komennot teknisen toteutuksen ensimmäiselle osiolle. Jokaista komentoa \
ajetaan merkkimäärille 6-18 tai kunnes Hashcat ei enää pysty. Lisää \
maskiin manuaalisesti yksi kirjain joka ajolla. 

hashcat -a 3 -m 3200 numbers.hash "?1?1?1?1?1?1" --custom-charset1 "?d" \
hashcat -a 3 -m 3200 alphaCaps.hash "?2?2?2?2?2?2" --custom-charset2 "?l?u" \
hashcat -a 3 -m 3200 AllChar.hash "?3?3?3?3?3?3" --custom-charset3 "?a"
 

**dictionary attack** \
Komennot toteutuksen toiselle osiolle.

hashcat -a 0 -m 3200 -r best64.rule bcrypt.hash passlist.txt \ 
hashcat -a 0 -m 6100 -r best64.rule whirlpool.hash passlist.txt \
hashcat -a 0 -m 17300 -r best64.rule sha3-256.hash passlist.txt
