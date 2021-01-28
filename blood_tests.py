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

interface()
