from pass_manage import encr_pass, read_pass_file, write_pass_to_file
from getpass import getpass

def add_new_user():
    """Add a new user to the password file."""
    username = input("Enter your username: ").strip()
    full_name= input("Enter your real/full name: ").strip()
    password= getpass("Enter Password: ").strip()

    datas=read_pass_file()
    for data in datas:
        if data[0] == username:
            print(f"Username '{username}' already exists.")
            return None
    
    encrypt_p=encr_pass(password)
    datas.append([username, full_name,encrypt_p])

    write_pass_to_file(datas)
    print("\nUser added successfully!")

#The main program starts here
    
if __name__=="__main__":
    add_new_user()