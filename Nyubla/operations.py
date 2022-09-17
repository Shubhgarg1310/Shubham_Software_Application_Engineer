
class Op:
    i=0
    def __init__(self):
        ch=int(input("Terraform is going to be available than press 1 else press 0: "))
        if(ch==1):
            self.i=1
        else:
            self.i=0
    
    def details(self):
        title=input("Enter the title of the appointmment: ")
        agenda=input("Enter the agenda: ")
        time=input("Enter the time to be scheduled: ")
        guest=input("Enter the guest name: ")
        
    
    def isAvailable(self):
        if(self.i==1):
            return True
        else:
            return False
    
    def appointment():
        if(Op.isAvailable()):
            print("Seeing upcoming appointments!!")
                 
        
