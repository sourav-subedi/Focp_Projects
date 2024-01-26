# this is the login page
from getpass import getpass
from pass_manage import encr_pass, read_pass_file

def user_login():
    """This function takes username and password from the user and validates it with the file
          and displays a access granted message if it matches with the database else gives an error message"""
    username= input("Username: ").strip()
    password = getpass("Password: ").strip()

    datas= read_pass_file()
    for data in datas:
        if data[0]==username and data[2]== encr_pass(password):
            print("Access granted.")
            return
    print("\nLogin failed. Please check your username or password.\n")

#The main program starts here
    
if __name__=="__main__":
    user_login()