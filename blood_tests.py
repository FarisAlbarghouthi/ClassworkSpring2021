def interface(): 

	print("Blood test analysis")
	while True:
                print("\nOptions")
                print("9-Quit")
                choice = input("Enter an option: ")
                if choice == "9":
                        return
                elif choice == "HDL":
                        HDL_driver()
                elif choice == "LDL":
                        LDL_driver()
                return

def HDL_driver():
        #get data
        #analyze data
        #output a result

        HDL = int(input("Enter your HDL level: "))
        if HDL>=60:
                print("Your HDL is normal")
        elif HDL>=40 & HDL <60:
                print("Your HDL is borderline low")
        elif HDL<40:
                print("Your HDL is low")
        return

def LDL_driver
        LDL = int(input("Enter your LDL level: "))
        if LDL>= 190:
                print("Your LDL is very high")
        elif 160<=LDL<=189:
                print("Your LDL is high")
        elif 130<=LDL<=159:
                print("Your LDL is borderline high")
        elif LDL<130:
                print("Your LDL is normal")
        return

                
interface()
