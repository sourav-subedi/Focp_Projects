# it performs the delete operation of the user details from the file
from pass_manage import read_pass_file, write_pass_to_file

def delete_user_data():
    """This function removes the user from the data file"""
    username= input("Enter username: ").strip()

    datas= read_pass_file()
    new_datas=[data for data in datas if data[0] != username]
    
    if len(new_datas) == len(datas):
        print('User not found')
    else:
        write_pass_to_file(new_datas)
        print('\n\tUser Deleted Successfully!')

#The main program starts here
        
if __name__=="__main__":
    delete_user_data()
            