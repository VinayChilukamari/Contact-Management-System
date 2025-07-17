import json

def display_contacts():
    for i in people: 
        print(i)

def add_person():
    person={}
    name=input("Enter your Name: ")
    person['name']=(name)
    age=input("Enter your Age: ")
    person['age']=age
    email_id=input("Enter your E-mail ID: ")
    person['email-ID']=email_id
    
    people.append(person)
    
    with open("contacts.json", "w") as f:
        json.dump({"contacts": people},f)
    
def delete_person(people):
    for index, person in enumerate(people):
        print(f"{index + 1} : {person['name']} | {person['age']} | {person['email-ID']}")
        
    if len(people)==0:
        print()
        print("Contact list is empty")
        print()
    else:
        while True:
            try:
                number=int(input("Enter the number of the person you want to delete: ")) 
                if number<=0 or number>len(people):
                    print()
                    print("Invalid number, index out range")
                    print()
                else:
                    break
            except Exception as e:
                print()
                print("Invalid number, enter an integer value")
                print()
        people.pop(number-1)
    with open("contacts.json", "w") as f:
        json.dump({"contacts": people},f)

def search_person(people):
    while True:
        result=[]
        search_by=input("Do you want to search by 'NAME', 'AGE', 'EMAIL-ID'? or enter 'q' to exit: ").lower()
        print()
        if search_by=='name':
            search_name=input("Do you want to search by 'FIRST NAME', 'LAST NAME', or 'FULL NAME'? (first/last/full): ").lower()
            print()
            if search_name=='first name' or search_name=='first':
                first_name=input("Enter the 'first name' of the person you want to search: ")
                print()
                for person in people:
                    if first_name == person["name"][0:len(first_name)]:
                        result.append(person)
                break
            elif search_name =='last name' or search_name=='last':
                last_name=input("Enter the 'last name' of the person you want to search: ")
                print()
                # print(last_name)
                for person in people:
                    if last_name == person["name"][-len(last_name):]:
                        result.append(person)
                break
            elif search_name =='full name' or search_name=='full':
                last_name=input("Enter the 'full name' of the person you want to search: ")
                print()
                
                for person in people:
                    if last_name == person["name"]:
                        result.append(person)
                break
            else:
                print()
                print("Invalid search")
                print()
        elif search_by=='age':
                age_inp=input("Enter the 'age' of the person you want to search: ")
                print()
                for person in people:
                    if age_inp==person['age']:
                        result.append(person)
                break
        elif search_by=='email-id':
            pass
        elif search_by =='q':
            break
        else:
            print("Invalid search")
            print()
            
        
    if len(result)==0:
        print()
        print("Person not found.\nNote: search is case-sensitive")
        print()
    else:
        print()
        print(result)
        print()
            
                
    
        
def change(people):
    pass

print("Hi, WELCOME to the Contact Management System")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]
   
while True:
    # size=len(people)
    print()
    print(f"Contact list size is: {len(people)}")
    print()
    action=input("Do you want to 'VIEW', 'ADD', 'CHANGE', 'DELETE', 'SEARCH' a person, or Enter 'q' to exit: ").lower()
    print()
    if action=='add':
        add_person()
        print()
        print("Person added!")
        print()
    elif action=='delete':
        delete_person(people)
        print()
        print("Person deleted!")
        print()
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
        print()
    

# print(people)