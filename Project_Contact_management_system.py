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
        print("Contact list is empty")
    else:
        while True:
            try:
                number=int(input("Enter the number of the person you want to delete: ")) 
                if number<=0 or number>len(people):
                    print("Invalid number, index out range")
                else:
                    break
            except Exception as e:
                print("Invalid number, enter an integer value")
        people.pop(number-1)
    with open("contacts.json", "w") as f:
        json.dump({"contacts": people},f)

def search_person(people):
    while True:
        result=[]
        search_by=input("Do you want to search by 'NAME', 'AGE', 'EMAIL-ID'? or enter 'q' to exit: ").lower()
        if search_by=='name':
            first_or_last=input("Do you want to search by 'FIRST NAME' or 'LAST NAME'? (first/last): ").lower()
            if first_or_last=='first name' or first_or_last=='first':
                first_name=input("Enter the 'first name' of the person you want to search: ")
                for person in people:
                    if first_name == person["name"][0:len(first_name)]:
                        result.append(person)
                break
            elif first_or_last =='last name' or first_or_last=='last':
                last_name=input("Enter the 'last name' of the person you want to search: ")
                print(last_name)
                for person in people:
                    if last_name == person["name"][-len(last_name):]:
                        result.append(person)
                break
        elif search_by=='age':
            try:
                age_inp=float(input("Enter the 'age' of the person you want to search: "))
                for person in people:
                    if age_inp==person['age']:
                        result.append(person)
                break
            except Exception as e:
                print(e)
        elif search_by=='email-id':
            pass
        elif search_by =='q':
            break
            
        
    if len(result)==0:
        print("Person not found.\nNote: search is case-sensitive")
    else:
        print(result)
            
                
    
        
def change(people):
    pass

print("Hi, WELCOME to the Contact Management System")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]
   
while True:
    # size=len(people)
    print(f"Contact list size is: {len(people)}")
    action=input("Do you want to 'VIEW', 'ADD', 'CHANGE', 'DELETE', 'SEARCH' a person, or Enter 'q' to exit: ").lower()
    if action=='add':
        add_person()
        print("Person added!")
    elif action=='delete':
        delete_person(people)
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
        print("Invalid response, try again")
    

# print(people)