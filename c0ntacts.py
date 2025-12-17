import time

    
def save_contact():
    contact_name=input("Enter contact name:\n ")
    with open("contacts.txt", "r") as file:
        contacts=file.readlines()

    exists= False

    for contact in contacts:
        if contact_name.lower() in contact.lower():
            exists= True
            
            break

    if exists:
        print("this name already exists")
    else:
        contact_number=input("Enter contact number:\n ")
        #save contact
        with open("contacts.txt","a") as file:
            file.write(f"{contact_name}: {contact_number}\n")
            print("saving contact...")
            time.sleep(2)
            print("contact saved successfully")
                    

        
def view_contact():

    with open("contacts.txt","r") as file:
        print(file.read())

        
def search_contact():

    search=input("enter the name to search:\n")
    with open("contacts.txt", "r")as file:
        contacts=file.readlines()

        found=False
        
    for contact in contacts:
        if search.lower() in contact.lower():
            print("searching...")
            time.sleep(2)
            print("contact found:", contact.strip())
            found=True
            break
            
    else:
        print("contact not found")
        
        
def delete_contact():

    delete=input("enter contact(name) to delete\n").lower().strip()
    
    with open("contacts.txt", "r")as file:
        contacts=file.readlines()

        found= False
        updated_contacts=[]

    for contact in contacts:
        if delete.lower() in contact.lower():
            found= True
            confirmation = input("are you sure you want to delete this contact? yes/no\n")
            if confirmation.lower().strip()=="yes":
                
                print("deleting...")
                time.sleep(2)
                print("contact successfully deleted")
                
            else:
                print("no contact deleted")
                updated_contacts.append(contact)
                with open("contacts.txt", "w") as file:
                    file.writelines(updated_contacts)
        else:
            updated_contacts.append(contact)
            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)

    if not found:
        print("contact not found")

def exit_contact():
    print("exiting...")
    time.sleep(2)
    print("thank you for using the contact manager")
    exit()
            
while True:
    print("1. save contact")
    print("2. view contact")
    print("3. search contact")
    print("4. delete contact")
    print("5. exit")

    choice= input("enter your choice: ")  

    if choice=="1":
        save_contact()
    elif choice=="2":
        view_contact()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        delete_contact()
    elif choice=="5":
        exit_contact()
    else:
        print("invalid choice, please try again.")
                    
                
            
                    



