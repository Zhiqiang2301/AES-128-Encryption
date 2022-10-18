import math 
from AESencryptfunc import * 
if len(sys.argv) != 3:#takes in two arguments for the plaintext.txt file name and cipherhex.txt file name
    sys.exit("Error, script needs two command-line arguments. (Plaintext.txt File and cipherhex.txt File)")

file=open(sys.argv[1], "r")
message=(file.read())
print("Inside your plaintext message is:\n%s\n" % message)
file.close()

file2=open(sys.argv[2], "r")
message2=(file2.read())
print("Inside your plaintext message is:\n%s\n" % message2)
file2.close()

print(message == message2)