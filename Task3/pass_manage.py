# This is a common module for password related operational function
import codecs

def encr_pass(password):
    """Encrypts the message with rot_13 encryption method"""
    return codecs.encode(password,"rot_13")

# def decr_pass(encoded_password):
#     return codecs.decode(encoded_password,"rot_13")

def read_pass_file(filename="passwd.txt"):
    """Read the content of passwd file and return list of the individual data in the line of file"""
    with open(filename,"r") as file:
        lines = file.readlines()
        return [line.strip().split(":") for line in lines]

def write_pass_to_file(data, filename="passwd.txt"):
    """Write the given data to the passwd file"""
    with open(filename,'w') as file:
        file.write("\n".join([":".join(i) for i in data]))