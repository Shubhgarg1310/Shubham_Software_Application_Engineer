if __name__=="__main__":
    print("===============================================================")
    print("Enter 1 to Sign Up")
    print("Enter 2 to Sign In")
    print("Enter 0 to exit")

    entry_choice = input("Enter your choice : ")
    if entry_choice.isdigit() and  int(entry_choice) == 1:
        Authenticate.sign_up()
    elif entry_choice.isdigit() and  int(entry_choice) == 2:
        Authenticate.login()
    elif entry_choice.isdigit() and  int(entry_choice) == 0:
        exit()
    else:
        print("Invalid choice, try again...")
        