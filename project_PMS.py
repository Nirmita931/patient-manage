
save = "data.txt"
def record(patient_id, first_name, last_name, address, gender, contact):
    fw = open(save, "a")
    fw.write("%1s%20s%20s%20s%20s%20s\n" %(patient_id, first_name, last_name, address, gender, contact))
    fw.close()

write = "paymentdata.txt"
def append(patient_id, invoice_id, credit_no, bill_amount):
    fw = open(write, "a")
    fw.write("%1s%20s%20s%20s\n" % (patient_id, invoice_id, credit_no, bill_amount))
    fw.close()

while True:
    print("1. Physician Login\n")
    print("2. Accountant Login\n")
    print("3. Receptionist Login\n")
    Login = input("Please choose 1 for physician login and 2 or accountant login\n")
    print(Login)
    if Login == "1":
        print("Please fulfill the requirements\n")


        username = input("Please enter the valid Username\n")
        print(username)
        password= input("Please enter the valid Passowrd\n")
        print(password)

        if (username, password) == ("a","a"):
            print("Welcome to Prudent Healthcare Service", username)

            print("\n1. New Patient")
            print("2. Old Patient\n")
            choose_patient = input("Choose '1' for new patient and '2' for old patient\n")
            print(choose_patient)
            if choose_patient == "1":
                print("New Patient\n")

                print("Please follow the following instructions to register new patient\n")

                patient_id = input("Patient ID\n")
                print(patient_id)
                first_name = input("First Name\n")
                print(first_name)
                last_name = input("Last Name\n")
                print(last_name)
                address = input("Address\n")
                print(address)
                gender = input("Gender\n")
                print(gender)
                contact = input("Contact\n")
                print(contact)

                record(patient_id, first_name, last_name, address, gender, contact)
                print("New patient with patient id",patient_id, "has been registered\n")


            elif choose_patient == "2":
                print("Old Patient\n")

                res = open("data.txt")
                extract = input("Please input patient ID\n")

                for each_line in res:
                    (patient_id, first_name, last_name, address, gender, contact) = each_line.split()
                    if(patient_id == extract):
                        print(patient_id, first_name, last_name, address, gender, contact)
                res.close()


            else:
                print("Error")


    elif Login == "2":
        print("Please fulfill the requirements\n")

        username = input("Please enter the valid Username\n")
        print(username)
        password = input("Please enter the valid Password\n")
        print(password)

        if (username, password) == ("a","a"):
            print("Welcome to Prudent Healthcare Service", username)

            res = open("data.txt")
            extract = input("Please input patient ID\n")
            for each_line in res:
                (patient_id, first_name, last_name, address, gender, contact) = each_line.split()
                if (patient_id == extract):
                    print(patient_id, first_name, last_name, address, gender, contact)
            res.close()


        payment = input("Check whether the payment is done by cash or credit.\n1. Cash\n2. Credit\nChoose '1' for payment done by cash and '2' for payment done by credit\n")
        print(payment)

        if payment == "1":
            print("Payment is done by cash.\nPlease record the information in the file\n")

            print("Please follow the following instructions to record information about payment process\n")

            patient_id = input("Patient ID\n")
            print(patient_id)
            invoice_id = input("Invoice Id\n")
            print(invoice_id)
            credit_no = input("Credit Number\n")
            print(credit_no)
            bill_amount = input("Total Bill Amount\n")
            print(bill_amount)

            append(patient_id, invoice_id, credit_no, bill_amount)
            print("Payment information of the patient with Patient Id",patient_id, "is recorded in the file")


        elif payment == "2":
            print("Payment is done by credit.\nPlease record the information in the file\n")

        else:
            print("Error")



    else:
        print("Error")

