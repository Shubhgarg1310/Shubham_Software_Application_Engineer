import bcrypt
import maskpass
from config import get_file_data,write_to_file;
from operations import Op

class Authenticate:
    def login():
        name = input("Enter the user name : ")
        
        file_data = get_file_data()
        
        if not name in file_data.keys():
            print("No such user found...!")
            return False

        password=maskpass.advpass().encode('utf-8')
        tries = 2
        while not bcrypt.checkpw(password, file_data[name]["password"].encode('utf-8')):
            if tries == 0:
                print("Incorrect password, try again !")
                return False
            print(f'Invalid password, {tries} tries left')
            tries -= 1
            password= maskpass.advpass().encode('utf-8')

        print("\nHello ", name, " : \n")
        
        # user_op = UserOperations()
        # user_op.show_unfinished_tasks(name)

        # while True:
        #     user_command = Choice().get_users_choice()
        #     if user_command==0:
        #         return
        #     Perform.operation_type(user_command, name)
        print("Do you want to schedule an appointment with other terraformers!!")
        print("Press 1 for Yes: ")
        print("Press 2 for No: ")
        ch=int(input("Enter choice: "))
        if ch==1:
            Op.details() 
            print("Do you want to update your password\npress 1 for it: ")
            ele=int(input("Enter choice: "))
            if(ele==1):
                login()
            
        
           
        elif ch==2:
            exit()
        


    def sign_up():
        file_data = get_file_data()
        username = input("Enter the Username, all smallcase : ")
        username=username.lower()
        while username in file_data.keys():
            print("User already exists, try another username")
            username = input("Enter the Username : ")

        password= maskpass.advpass()
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        
        hashed = bcrypt.hashpw(bytes, salt).decode()
        new_user_entry = {
            "password": hashed,
            "tasks": []
        }
        
        file_data[username] = new_user_entry
        write_to_file(file_data)


if __name__=="__main__":
    print("===============================================================")
    print("Enter 1 to Sign Up")
    print("Enter 2 to Sign In")
    print("Enter 0 to exit")
    
    while True:
        entry_choice = input("Enter your choice : ")
        if entry_choice.isdigit() and  int(entry_choice) == 1:
            Authenticate.sign_up()
        elif entry_choice.isdigit() and  int(entry_choice) == 2:
            Authenticate.login()
        elif entry_choice.isdigit() and  int(entry_choice) == 0:
            exit()
        else:
            print("Invalid choice, try again...")
        
