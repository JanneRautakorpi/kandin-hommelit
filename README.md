**extended-leet.rule**: Generoitu Hashcatin processor maskin avulla seuraavalla komennolla: mp64.bin -o extended-leet.rule 'sa4 se3 si1 sl1 so0 $s'. \
**100md5salasanat.txt**: Sisältää 100 MD5-tiivistettä, jotka ovat satunnaisia sanoja suomen kielen sanakirjasta. Sanat ovat Leet-muunnettuja extended-leet.rule mukaisesti ja loppuun on lisätty satunnainen erikoismerkki.\
**hashlist.hash**: sisältää tiivisteet, jotka murretaan.\
**run_hashcat.py**: Python skripti, joka implementoi timeout-ominaisuuden Hashcatin ajoon.
