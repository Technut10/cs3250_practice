# I have added a python boilerplate, woohoo
import base64

print("Cove was here")

print("Hello, World!")

print("this is something new")

def printMore(string):
    print(string)
    
def printEvenMore(string, string2):
    print(string, string2)
    print("HOLY COW THAT'S A LOT OF PRINTING")

def encrypt_string(someMessage: str):
    if type(someMessage) != str:
        raise TypeError('Input must be a string')
    
    return base64.encodebytes(someMessage.encode('utf-8'))
