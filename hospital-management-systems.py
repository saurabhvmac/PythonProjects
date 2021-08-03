from os import system
import pickle
class Hospital: 
    p_id = None
    f_name = None
    l_name = None
    p_sex = None
    age = None
    blood = None
    mobile = None
    problem = None
    def getpatientdata(self):
        print("=====================================================")
        print("|-- HOSPITAL MANAGEMENT SYSTEM --|")
        print("=====================================================")
        print("\t\t Enter the data for the Patient")
        self.p_id=int(input("Patient ID: "))
        self.f_name=input("Name: ")
        self.l_name=input("Last Name: ")
        self.p_sex=input("Sex: ")
        self.age=int(input("Age: "))
        self.blood=input("Blood Group: ")
        self.mobile=int(input("Mobile Number: "))
        self.problem=input("Problem: ")
    def showpatientdata(self):
        print("=====================================================")
        print("|-- HOSPITAL MANAGEMENT SYSTEM --|")
        print("=====================================================")
        print("\t\t Pateint Information")
        print("\n")
        print(f"  Patient ID:{self.p_id} ")
        print(f"  FirstName:{self.f_name} ")
        print(f"  Last Name:{self.f_name} ")
        print(f"  Sex:{self.f_name} ")
        print(f"  Age:{self.f_name} ")
        print(f"  Blood Group:{self.f_name} ")
        print(f"  Mobile:{self.f_name} ")
        print(f"  Problem:{self.f_name} ")
        print("==================================================")

def mainmenu(): 
    global Choice
    system('cls')
    print("=====================================================")
    print("       |-- HOSPITAL MANAGEMENT SYSTEM --|")
    print("=====================================================")
    print("                 ADMIN LOGED IN")
    print("=====================================================")
    print("                   MAIN MENU")
    print("\n  [1] Add New Patine")
    print("  [2] Add Patient to Emergency")
    print("  [3] Display All Patient")
    print("  [4] Display Patient by ID")
    print("  [5] Discharge Patient")
    print("  [6] Log Out")
    Choice = int(input("Enter Your Choice: "))
    if Choice==1:
        newpatient()
    elif Choice==2:
        EmergencyPatient()
    elif Choice==3:
        showallpatiets()
    elif Choice==4:
        Showpatientbyid()
    elif Choice==5:
        dischargepatient()
    else:
        mainmenu()

def newpatient():
    patient = Hospital()
    patient.getpatientdata()
    with open("hospital.dat",'wb') as hs:
        pickle.dump(patient,hs)
    print("\n Patient Added in Record  ")
    he=input("\n\t Press Enter: ")
    mainmenu()

def EmergencyPatient():
    print("\n Emergency   ")
    he=input("\n\t Press Enter: ")
    mainmenu()
def Showpatientbyid():
    print("\n Patient by id  ")
    he=input("\n\t Press Enter: ")
    mainmenu()
def showallpatiets():
    patient = Hospital()
    print("\n Patient all  ")
    with open("hospital.dat", "rb") as hs:
        pickle.load(hs)
        patient.showpatientdata()
    he=input("\n\t Press Enter: ")
    mainmenu()
def dischargepatient():
    print("\n Patient discharged  ")
    he=input("\n\t Press Enter: ")
    mainmenu()


#MAIN
print("=====================================================")
print("|-- HOSPITAL MANAGEMENT SYSTEM --|")
print("=====================================================")
mainmenu()
login=int(input("Login ID: "))
pin=int(input("Pin: "))
if login==1234 and pin==1234:
    mainmenu()
else:
    print("You have Entered Wrong Password")

