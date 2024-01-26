# This file performs the password change operations
from getpass import getpass
from pass_manage import encr_pass, read_pass_file, write_pass_to_file

def password_change():
    """This function asks the user for username and password and allows user to change their 
    current password with a new one"""
    username=input("Enter username: ").strip()
    current_pass=getpass("Current Password: ").strip()

    datas= read_pass_file()
    for data in datas:
        if data[0]==username:
            found=True
            if data[2]==encr_pass(current_pass):
                new_password = getpass("New Password: ").strip()
                confirm_new_password = getpass("Confirm New Password: ").strip()

                if new_password==confirm_new_password:
                    data[2]=encr_pass(new_password)
                    write_pass_to_file(datas)
                    print("\nPassword changed successfully.")
                else:
                    print("\nPasswords do not match. Please try again.")
            else:
                print('\nWrong Current Password.\nPlease Try Again')
                return
        
#The main program starts here
            
if __name__=="__main__":
    password_change()