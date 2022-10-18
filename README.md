# AES-128-Encryption



Resource(s) Used: </br>
-BitVector class created by Avinash Kak (kak@purdue.edu) at https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html </br>
-Nist Announcement Publication of AES in 2001 at http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf </br>

Summary:</br>
Two scripts in Python to encrypt/decrypt using the 128 bits AES algorithm, ECB mode. For the encryption, an ascii plaintext file is taken as the input, then an encrypted hex file is outputted. For the decryption, a ciphertext hex file is taken as the input, then a decrypted ascii file is outputted.</br>

Notes: </br> 
-ECB is not considered secure since it has vulnerabilities in encrypting the same plaintext block. Encrypting the same plaintext block will create the same block of ciphertext. Possible future improvement is to use a more psuedo random mode other than ECB.</br>
<br />
--------------------Demonstration--------------------<br />
Running AESencrypt.py Script: <br />
![encrypt](/Demo/1.encrypt.png)
<br /><br /><br />
Running AESencrypt.py Script: <br />
![decrypt](/Demo/2.decrypt.png)
<br /><br /><br />
Checking plaintext1.txt File with plaintext2.txt File: <br />
![check](/Demo/3.check.png)
<br /><br /><br />

