option = 0
list_1= []
while option!=4:
    print("Contact Book\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit\n")
    option = int(input(" Choose an option: "))
    if option == 1:
        name = input("Enter the name: ")
        phoneno = input("Enter the phone number: ")
        list_1.append(name)
        list_1.append(phoneno)
        print("Contact saved \n ")
    elif option == 2 and list_1!=[]:
        print("Contacts:")
        for i in range(0, len(list_1), 2):
           
            print(f"- {list_1[i]} - {list_1[i+1]}\n")
        else:
            print("Contact not found")    
    elif option ==3:
        search = input("Enter the name: ")
        if search in list_1:
            j = list_1.index(search)
            print(f"Found - {list_1[j]} - {list_1[j+1]}")
            
    elif option ==4:
        break
else:
    print("Invalid option. Please try again.\n")
    
    