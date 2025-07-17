import json
# contacts.json file is used throughout this code

def json_read():# this funtion reads data from contacts.json file and returns as list.
    with open("contacts.json", "r") as f:
        return json.load(f)["contacts"]

def json_dump():# this funtion loads data to contacts.json file after the changes made by user.
    with open("contacts.json", "w") as f:
        json.dump({"contacts": people},f)

def display_contacts():# this funtion displays data available in contacts.json file.
    # for index, person in enumerate(people):
    #     print(f"{index + 1} : {person['name']} | {person['age']} | {person['email-ID']}")
    for index, person in enumerate(people):
        print(index+1,"-->",person)

def index_num_inp(text):# this funtion allows only integer input by validating its data type and returns only integer.
    while True:
        try:
            print()
            number=int(input(f"Enter the number of the person you want to {text}: "))
            if number<=0 or number>len(people):
                print()
                print("Invalid number, index out range")
            else:
                break
        except Exception as e:
            print()
            print("Invalid number, enter an integer value")

    return number

def add_person():# this function allows user to add new person to contacts.json file.
    person={}
    name=input("Enter your Name: ")
    person['name']=(name)
    age=input("Enter your Age: ")
    person['age']=age
    email_id=input("Enter your E-mail ID: ")
    person['email-ID']=email_id
    
    people.append(person)
    
    json_dump()
    
def delete_person(people):# this function allows user to delete specified person from contacts.json file.
    display_contacts()
        
    if len(people)==0:
        print()
        print("Contact list is empty")
    else:
        number=index_num_inp('delete') # function to get the index number of the list to delete
        people.pop(number-1)
    json_dump()

def search_person(people):# this functions allows user to search the person from contacts.json file.
    while True:
        result=[]
        print()
        search_by=input("Do you want to search by 'NAME', 'AGE', 'EMAIL-ID'? or enter 'q' to exit: ").lower()
        if search_by=='name':
            print()
            search_name=input("Do you want to search by 'FIRST NAME', 'LAST NAME', or 'FULL NAME'? (first/last/full): ").lower()
            if search_name=='first name' or search_name=='first':
                print()
                first_name=input("Enter the 'first name' of the person you want to search: ")
                for person in people:
                    if first_name == person["name"][0:len(first_name)]:
                        result.append(person)
                break
            elif search_name =='last name' or search_name=='last':
                print()
                last_name=input("Enter the 'last name' of the person you want to search: ")
                # print(last_name)
                for person in people:
                    if last_name == person["name"][-len(last_name):]:
                        result.append(person)
                break
            elif search_name =='full name' or search_name=='full':
                print()
                last_name=input("Enter the 'full name' of the person you want to search: ")
                for person in people:
                    if last_name == person["name"]:
                        result.append(person)
                break
            else:
                print()
                print("Invalid search")
        elif search_by=='age':
            print()
            age_inp=input("Enter the 'age' of the person you want to search: ")
            for person in people:
                if age_inp==person['age']:
                    result.append(person)
            break
        elif search_by=='email-id':
            print()
            email_inp=input("Enter the 'email-ID' of the person you want to search: ")
            for person in people:
                if email_inp==person['email-ID']:
                    result.append(person)
            break
            
        elif search_by =='q':
            break
        else:
            print()
            print("Invalid search")
            
        
    if len(result)==0:
        print()
        print("Person not found.\nNote: search is case-sensitive")
    else:
        print()
        for i in result:
            print(i)
        print()
            
def change(people):# this functions allows user to change persos's attribute from contacts.json file.
    display_contacts()
    number=index_num_inp('change')
    # print(number)
    for person in people:
        change_index=number-1
        if change_index==people.index(person):
            while True:
                print()
                change_inp=input("Specify what do you want to change? 'NAME', 'AGE', or 'EMAIL-ID'?: ").lower()
                if change_inp=='name':
                    o_name=people[change_index]['name']
                    u_name=''
                    print()
                    change_by=input("Do you want to change by 'FIRST NAME', 'LAST NAME', or 'FULL NAME'? (first/last/full): ").lower()
                    if change_by=='first name' or change_by=='first':
                        update=o_name.split()
                        update.remove(update[0])
                        print()
                        update.insert(0,input("Enter the updated name: "))
                        u_name=' '.join(update)
                        people[change_index]['name']=u_name
                        json_dump()
                        print()
                        print("First name updated")
                        break
                    elif change_by=='last name' or change_by=='last':
                        
                        update=o_name.split()
                        if len(update)==1:
                            print()
                            print("Last name does not exist, please change in full name")
                            break
                        else:
                            update.remove(update[1])
                            print()
                            update.insert(1,input("Enter the updated name: "))
                            u_name=' '.join(update)
                            people[change_index]['name']=u_name
                            json_dump()
                            print()
                            print("Last name updated")
                            break
                    elif change_by=='full name' or change_by=='full':
                        print()
                        u_name=input("Enter the updated name: ")
                        people[change_index]['name']=u_name
                        json_dump()
                        print()
                        print("Name updated")
                        break
                    else:
                        print("Invalid input")
                        
                    
                elif change_inp=='age':
                    print()
                    people[change_index]['age']=input("Enter the updated age: ")
                    json_dump()
                    print()
                    print("Age updated")
                    break
                    
                elif change_inp=='email-id':
                    print()
                    people[change_index]['email-ID']=input("Enter the updated email-ID: ")
                    json_dump()
                    print()
                    print("Email-ID updated")
                    break
                else:
                    print()
                    print("Invalid input, try again")
                
        

print("Hi, WELCOME to the Contact Management System")

people= json_read()
# print(people)
   
while True:
    # size=len(people)
    print()
    print(f"Contact list size is: {len(people)}")
    print()
    action=input("Do you want to 'VIEW', 'ADD', 'CHANGE', 'DELETE', 'SEARCH' a person, or Enter 'q' to exit: ").lower()
    if action=='add':
        add_person()
        print()
        print("Person added!")
    elif action=='delete':
        delete_person(people)
        print()
        print("Person deleted!")
    elif action=='search':
        search_person(people)
    elif action=='view':
        display_contacts()
    elif action=='change':
        change(people)
    elif action=='q':
        break
    else:
        print()
        print("Invalid response, try again")
    
# print(people)