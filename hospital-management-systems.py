
from os import system
import sqlite3
from contextlib import closing

class Hospital: 
    def getpatientdata(self):
        print("=====================================================")
        print("|-- HOSPITAL MANAGEMENT SYSTEM --|")
        print("=====================================================")
        print("\t\t Enter the data for the Patient")
        self.p_id=int(input("Patient ID: "))
        self.f_name=input("Name: ")
        self.l_name=input("Last Name: ")
        self.p_sex=input("Sex: ")
        self.p_age=int(input("Age: "))
        self.p_blood=input("Blood Group: ")
        self.p_mobile=int(input("Mobile Number: "))
        self.p_problem=input("Problem: ")

def showpatientdata(p_id, f_name, l_name, p_sex, p_age, p_blood, p_mobile, p_problem):
    print("=====================================================")
    print("\t\t Pateint Information")
    print("\n")
    print(f"  Patient ID:   {p_id} ")
    print(f"  FirstName:    {f_name} ")
    print(f"  Last Name:    {l_name} ")
    print(f"  Sex:          {p_sex} ")
    print(f"  Age:          {p_age} ")
    print(f"  Blood Group:  {p_blood} ")
    print(f"  Mobile:       {p_mobile} ")
    print(f"  Problem:      {p_problem} ")
    print("==================================================")
    print("\n")

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
    print("  [2] Display All Patient")
    print("  [3] Display Patient by ID")
    print("  [4] Discharge Patient")
    print("  [5] Log Out")
    Choice = int(input("Enter Your Choice: "))
    if Choice==1:
        newpatient()
    elif Choice==2:
        showallpatiets()
    elif Choice==3:
        Showpatientbyid()
    elif Choice==4:
        dischargepatient()
    else:
        main()

def newpatient():
    system('cls')
    patient = Hospital()
    patient.getpatientdata()
    conn = sqlite3.connect('hospital.db')
    conn.execute("INSERT INTO hospital (id,fname,lname,sex,age,blood,mobile,problem)\
            VALUES (?,?,?,?,?,?,?,?)",(patient.p_id,patient.f_name,patient.l_name,patient.p_sex,patient.p_age,patient.p_blood,patient.p_mobile,patient.p_problem))
    conn.commit()
    conn.close()
    print("\n Patient Added in Record  ")
    he=input("\n\t Press Enter: ")
    mainmenu()

def Showpatientbyid():
    system('cls')
    print("=====================================================")
    print("       |-- HOSPITAL MANAGEMENT SYSTEM --|")
    print("=====================================================")
    patient_id = int(input("Enter Patient ID : "))
    conn = sqlite3.connect('hospital.db')
    row = conn.execute("SELECT * FROM hospital WHERE id = ?",(patient_id,)).fetchall()
    for r in row:
        p_id = r[0]
        f_name = r[1]
        l_name = r[2]
        p_sex = r[3]
        p_age = r[4]
        p_blood = r[5]
        p_mobile = r[6]
        p_problem = r[7]
        showpatientdata(p_id, f_name, l_name, p_sex, p_age, p_blood, p_mobile, p_problem)
    conn.commit()
    conn.close()    
    print("\n Patient by id  ")
    he=input("\n\t Press Enter: ")
    mainmenu()

def showallpatiets():
    system('cls')
    print("=====================================================")
    print("       |-- HOSPITAL MANAGEMENT SYSTEM --|")
    conn = sqlite3.connect('hospital.db')
    row = conn.execute("SELECT * FROM hospital").fetchall()
    for r in row:
        p_id = r[0]
        f_name = r[1]
        l_name = r[2]
        p_sex = r[3]
        p_age = r[4]
        p_blood = r[5]
        p_mobile = r[6]
        p_problem = r[7]
        showpatientdata(p_id, f_name, l_name, p_sex, p_age, p_blood, p_mobile, p_problem)
    conn.commit()
    conn.close()
    he=input("\n\t Press Enter: ")
    mainmenu()

def dischargepatient():
    system('cls')
    print("=====================================================")
    print("       |-- HOSPITAL MANAGEMENT SYSTEM --|")
    print("=====================================================")
    patient_id = int(input("Enter Patient ID to discharge "))
    conn = sqlite3.connect('hospital.db')
    conn.execute("DELETE from hospital where ID = ?",(patient_id,))
    print("\n")
    print(f"Patient with ID {patient_id} Discharged")
    # discharge patinet go into a seperate table
    conn.commit()
    conn.close()
    he=input("\n\t Press Enter: ")
    mainmenu()


def main():
    system('cls')
    print("=====================================================")
    print("|-- HOSPITAL MANAGEMENT SYSTEM --|")
    print("=====================================================")
    login=int(input("Login ID: "))
    pin=int(input("Pin: "))
    if login==1234 and pin==1234:
        mainmenu()
    else:
        print("You have Entered Wrong Password")

main()
