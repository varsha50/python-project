cusID=[]
cusAge=[]
cusName=[]
cusMob=[]
cusAddress=[]
cusCity=[]
cusPincode=[]
cusEmail=[]

def addCust(id,age,name,mob,address,city,pincode,email):  #function for add customer
    cusID.append(id)
    cusAge.append(age)
    cusName.append(name)
    cusMob.append(mob)
    cusAddress.append(address)
    cusCity.append(city)
    cusPincode.append(pincode)
    cusEmail.append(email)

def getId():  #validation for ID
    while(1):
        id=input("Enter customer's ID:")
        if(id in cusID):
            print("ID already exists, Try again")
        elif(id.isnumeric()):
            return id
        else:
            print("Entered ID must be numeric only")

def getAge():  #validation for age
    while(1):
        age=input("Enter customer's Age:")
        if(age.isnumeric()):
            if(int(age)>=10 and int(age)<=100):
                return age
            else:
                print("Entered Age must bewteen(10-100) only")
        else:
            print("Entered Age must be numeric only")

def getName():  #validation for name
    while(1):
        name=input("Enter customer's Name:")
        if(name.isalpha()):
            if(len(name)>1):
                return name
            else:
                print("Entered name length must be 2 alphabet atleast")
        else:
            print("Entered Age must be alphabet only")

def getMob():  #validation for mobile no.
    while(1):
        mob=input("Enter customer's Mobile no:")
        if(mob in cusMob):
            print("Mobile no. already exist, Try again")
        elif(mob.isnumeric()):
            if(len(mob)==10):
                return mob
            else:
                print("Entered Mobile no. must be 10 digits only")
        else:
            print("Entered Mobile no. must be numeric only")

def getAdd():  #validation for address
    while(1):
        address=input("Enter customer's address:")
        if(len(address)>0):
            return address
        else:
            print("Entered Address length must be 1 alphabet atleast")

def getCity():  #validation for city
    while(1):
        city=input("Enter customer's City:")
        if(city.isalpha()):
            if(len(city)>1):
                return city
            else:
                print("Entered City length must be 2 alphabet atleast")
        else:
            print("Entered City must be alphabet only")

def getPin():  #validation for pincode
    while(1):
        pincode=input("Enter customer's PinCode:")
        if(pincode.isnumeric()):
            if(len(pincode)==6):
                return pincode
            else:
                print("Entered PinCode length must be 6 digits only")
        else:
            print("Entered PinCode must be numeric only")

def getEmail():  #validation for email
    while(1):
        email=input("Enter customer's Email ID:")
        if(email in cusEmail):
            print("Email ID is already exists, Try again")
        elif(len(email) > 10):
            if('@gmail.com' in email):
                return email
            else:
                print("Please include '@gmail.com' in Email ID")
        else:
            print("Entered Email ID length must be 11 digits atleast")

def searchCustId(id):
    index=cusID.index(id)
    return index

def searchCustName(name1):
    index=cusName.index(name1)
    return index

def searchCustMob(mob):
    index=cusMob.index(mob)
    return index

def searchCustEmail(email):
    index=cusEmail.index(email)
    return index

def delCustId(id1):
    index=cusID.index(id1)
    cusID.pop(index)
    cusAge.pop(index)
    cusName.pop(index)
    cusMob.pop(index)
    cusAddress.pop(index)
    cusCity.pop(index)
    cusPincode.pop(index)
    cusEmail.pop(index)

def delCustName(name1):
    index=cusName.index(name1)
    cusID.pop(index)
    cusAge.pop(index)
    cusName.pop(index)
    cusMob.pop(index)
    cusAddress.pop(index)
    cusCity.pop(index)
    cusPincode.pop(index)
    cusEmail.pop(index)

def delCustMob(mob1):
    index=cusMob.index(mob1)
    cusID.pop(index)
    cusAge.pop(index)
    cusName.pop(index)
    cusMob.pop(index)
    cusAddress.pop(index)
    cusCity.pop(index)
    cusPincode.pop(index)
    cusEmail.pop(index)

def delCustEmail(email1):
    index=cusEmail.index(email1)
    cusID.pop(index)
    cusAge.pop(index)
    cusName.pop(index)
    cusMob.pop(index)
    cusAddress.pop(index)
    cusCity.pop(index)
    cusPincode.pop(index)
    cusEmail.pop(index)

def modifyCustID(id2, age2, name2, mob2, address2, city2, pincode2, email2):
    index = cusID.index(id2)
    cusAge[index]=age2
    cusName[index]=name2
    cusMob[index]=mob2
    cusAddress[index]=address2
    cusCity[index]=city2
    cusPincode[index]=pincode2
    cusEmail[index]=email2

def modifyCustName(id2, age2, name2, mob2, address2, city2, pincode2, email2):
    index = cusName.index(name2)
    cusAge[index]=age2
    cusName[index]=name2
    cusMob[index]=mob2
    cusAddress[index]=address2
    cusCity[index]=city2
    cusPincode[index]=pincode2
    cusEmail[index]=email2

def modifyCustMob(id2, age2, name2, mob2, address2, city2, pincode2, email2):
    index = cusMob.index(mob2)
    cusAge[index]=age2
    cusName[index]=name2
    cusMob[index]=mob2
    cusAddress[index]=address2
    cusCity[index]=city2
    cusPincode[index]=pincode2
    cusEmail[index]=email2

def modifyCustEmail(id2, age2, name2, mob2, address2, city2, pincode2, email2):
    index = cusEmail.index(email2)
    cusAge[index]=age2
    cusName[index]=name2
    cusMob[index]=mob2
    cusAddress[index]=address2
    cusCity[index]=city2
    cusPincode[index]=pincode2
    cusEmail[index]=email2

while(1):
    print("1: Add Customer")
    print("2: Search Customer")
    print("3: Delete Customer")
    print("4: Modify Customer")
    print("5: Display All Customers")
    print("6: Exit")
    choice=input("Enter Choice 1 to 6:\n")

    if(choice=="1"): #Add Customer
        id=getId()
        age=getAge()
        name=getName()
        mob=getMob()
        address=getAdd()
        city=getCity()
        pincode=getPin()
        email=getEmail()
        addCust(id,age,name,mob,address,city,pincode,email)
        print("Customer added successfully")

    elif(choice=="2"): #Search Customer
        print("1. search by ID")
        print("2. search by Name")
        print("3. search by Ph.no.")
        print("4. search by Email ID\n")
        choice1=input("enter your choice")

        if(choice1=="1"):
            while(1):
                id=input("Enter Customer ID: ")
                if (id.isnumeric()):
                    if(id not in cusID):
                        print("ID does not exist, Try again")
                        break
                    else:
                        index = searchCustId(id)
                        print("Cust ID:",cusID[index]," Cust Age:",cusAge[index]," Cust Name:",cusName[index],
                              " Cust Mob:",cusMob[index]," Cust Address:",cusAddress[index]," Cust City:",cusCity[index],
                              " Cust PinCode:",cusPincode[index]," Cust Email ID:",cusEmail[index])
                        break
                else:
                    print("Entered ID must be numeric only")

        elif(choice1=="2"):
            while(1):
                name=input("Enter Customer Name:")
                if(name.isalpha()):
                    if(name not in cusName):
                        print("Name does not exist, Try again")
                        break
                    else:
                        index = searchCustName(name)
                        print("Cust ID:", cusID[index], " Cust Age:", cusAge[index], " Cust Name:", cusName[index],
                              " Cust Mob:", cusMob[index], " Cust Address:", cusAddress[index], " Cust City:",
                              cusCity[index]," Cust PinCode:", cusPincode[index], " Cust Email ID:", cusEmail[index])
                        break
                else:
                    print("Entered Name must be alphabet only")

        elif(choice1 == "3"):
            while(1):
                mob = input("Enter customer Ph.no.:")
                if(mob.isnumeric()):
                    if(len(mob)==10):
                        if (mob not in cusMob):
                            print("Ph.No. does not exist, Try again")
                            break
                        else:
                            index = searchCustMob(mob)
                            print("Cust ID:", cusID[index], " Cust Age:", cusAge[index], " Cust Name:", cusName[index],
                                  " Cust Mob:", cusMob[index], " Cust Address:", cusAddress[index], " Cust City:",
                                  cusCity[index], " Cust PinCode:", cusPincode[index], " Cust Email ID:",cusEmail[index])
                            break
                    else:
                        print("Please Enter Ph.no with 10 digits only")
                else:
                    print("Entered Ph.NO. must be numeric only")

        elif(choice1 == "4"):
            while (1):
                email = input("Enter Customer's Email ID:")
                if ('@gmail.com' in email):
                    if(len(email) > 10):
                        if (email not in cusEmail):
                            print("Email ID does not exists, Try again")
                            break
                        else:
                            index = searchCustEmail(email)
                            print("Cust ID:", cusID[index], " Cust Age:", cusAge[index], " Cust Name:", cusName[index],
                                  " Cust Mob:", cusMob[index], " Cust Address:", cusAddress[index], " Cust City:",
                                  cusCity[index], " Cust PinCode:", cusPincode[index], " Cust Email ID:",cusEmail[index])
                            break
                    else:
                        print("Entered Email ID length must be 11 atleast")

                else:
                    print("Please include '@gmail.com' in Email ID")
        else:
            print("Please Enter correct choice")
            print("1. Press For main menu")
            print("2. Press For exit the program")
            ip=input("Enter your choice:")
            if(ip=='1'):
                pass
            elif(ip=='2'):
                print("Thanks for using this")
                exit()
            else:
                print("Please Enter correct choice")


    elif(choice=="3"): #Delete Customer

        print("1. Delete by ID")
        print("2. Delete by Name")
        print("3. Delete by Ph.No")
        print("4. Delete by Email ID")
        choice2=input("Enter your choice:")

        if(choice2=='1'):
            while(1):
                id1=input("Enter Customer ID for Deletion")
                if (id1.isnumeric()):
                    if (id1 not in cusID):
                        print("ID does not exist, Try again")
                        break
                    else:
                         delCustId(id1)
                         print("Customer Deleted Successfully")
                         break
                else:
                    print("ID must be numeric only")

        elif (choice2 == '2'):
            while (1):
                name1 = input("Enter Customer Name for Deletion")
                if (name1.isalpha()):
                    if (name1 not in cusName):
                        print("Name does not exist, Try again")
                        break
                    else:
                        delCustName(name1)
                        print("Customer Deleted Successfully")
                        break
                else:
                    print("Name must be string only")

        elif (choice2 == '3'):
            while (1):
                mob1= input("Enter Customer PH.NO. for Deletion")
                if (mob1.isnumeric()):
                    if(len(mob1)==10):
                        if (mob1 not in cusMob):
                            print("Ph.No. does not exist, Try again")
                            break
                        else:
                            delCustMob(mob1)
                            print("Customer Deleted Successfully")
                            break
                    else:
                        print("Ph.No. must contains 10 Digits only")
                else:
                    print("Ph.No. must be numeric only")

        elif (choice2 == '4'):
            while (1):
                email1= input("Enter Customer Email ID for Deletion")
                if ('@gmail.com' in email1):
                    if (len(email1) > 10):
                        if (email1 not in cusEmail):
                            print("Email ID does not exist, Try again")
                            break
                        else:
                            delCustEmail(email1)
                            print("Customer Deleted Successfully")
                            break
                    else:
                        print("Entered Email ID length must be 11 atleast")

                else:
                    print("Please include '@gmail.com' in Email ID")


        else:
            print("Please Enter correct choice")
            print("1. Press For main menu")
            print("2. Press For exit the program")
            ip1=input("Enter your choice:")
            if(ip1=='1'):
                pass
            elif(ip1=='2'):
                print("Thanks for using this")
                exit()
            else:
                print("Please Enter correct choice")


    elif(choice=="4"):#Modify Customer

        print("1. Modify by ID")
        print("2. Modify by Ph.No")
        print("3. Modify by Email ID")
        choice3 = input("Enter your choice:")

        if(choice3=="1"):
            while (1):
                id2 = input("Enter Customer ID to Update all details:")
                if (id2.isnumeric()):
                    if (id2 not in cusID):
                        print("ID does not exist, Try again")
                        break
                    else:
                        age2 = input("Enter Customer Updated Age: ")
                        name2 = input("Enter Customer Updated Name: ")
                        mob2 = input("Enter Customer Ph.No: ")
                        address2 = input("Enter Customer Address: ")
                        city2 = input("Enter Customer City: ")
                        pincode2 = input("Enter Customer PinCode: ")
                        email2 = input("Enter Customer Email ID: ")
                        modifyCustID(id2, age2, name2, mob2, address2, city2, pincode2, email2)
                        print("Customer modified successfully")
                        break
                else:
                    print("ID must be numeric only")

        elif (choice3 == "2"):
            while (1):
                mob2 = input("Enter Customer Ph.No. to Update all details:")
                if (mob2.isnumeric()):
                    if(len(mob2)==10):
                        if (mob2 not in cusMob):
                            print("Ph.No. does not exist, Try again")
                            break
                        else:
                            age2 = input("Enter Customer Updated Age: ")
                            name2 = input("Enter Customer Updated Name: ")
                            mob2 = input("Enter Customer Ph.No: ")
                            address2 = input("Enter Customer Address: ")
                            city2 = input("Enter Customer City: ")
                            pincode2 = input("Enter Customer PinCode: ")
                            email2 = input("Enter Customer Email ID: ")
                            modifyCustID(id2, age2, name2, mob2, address2, city2, pincode2, email2)
                            print("Customer modified successfully")
                            break
                    else:
                        print("Ph.No. must include 10 digits only")
                else:
                    print("Ph.No. must be numeric only")

        elif(choice3=="3"):
            while (1):
                email2 = input("Enter Customer Email ID to Update all details:")
                if ('@gmail.com' in email2):
                    if (len(email2) > 10):
                        if(email2 not in cusEmail):
                            print("ID does not exist, Try again")
                            break
                        else:
                            age2 = input("Enter Customer Updated Age: ")
                            name2 = input("Enter Customer Updated Name: ")
                            mob2 = input("Enter Customer Ph.No: ")
                            address2 = input("Enter Customer Address: ")
                            city2 = input("Enter Customer City: ")
                            pincode2 = input("Enter Customer PinCode: ")
                            email2 = input("Enter Customer Email ID: ")
                            modifyCustID(id2, age2, name2, mob2, address2, city2, pincode2, email2)
                            print("Customer modified successfully")
                            break
                    else:
                        print("Entered Email ID length must be 11 atleast")
                else:
                    print("Please include '@gmail.com' in Email ID")

        else:
            print("Please Enter correct choice")
            print("1. Press For main menu")
            print("2. Press For exit the program")
            ip2 = input("Enter your choice:")
            if (ip2 == '1'):
                pass
            elif (ip2 == '2'):
                print("Thanks for using this")
                exit()
            else:
                print("Please Enter correct choice")

    elif(choice=="5"): #Display All Customers
        for i in range(len(cusID)):
            print("Cust ID: ", cusID[i], "\t\tCust Age: ",cusAge[i],"\t\tCust Name: ",cusName[i], "\t\tCust Mob: ",cusMob[i],
                  "\t\tCust Address: ", cusAddress[i], "\t\tCust City: ",cusCity[i], "\t\tCust PinCode: ",cusPincode[i],
                  "\t\tCust Email ID: ", cusEmail[i])

    elif(choice=="6"):
        exit()

    else:
        print("Please Enter correct choice")
        print("1. Press For main menu")
        print("2. Press For exit the program")
        ip3 = input("Enter your choice:")
        if (ip3 == '1'):
            pass
        elif (ip3 == '2'):
            print("Thanks for using this")
            exit()
        else:
            print("Please Enter correct choice")