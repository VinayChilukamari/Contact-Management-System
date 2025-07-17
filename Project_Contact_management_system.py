import json

def display_contacts():
    with open("contacts.json","r") as f:
        people=f.read()
    
    print(people)

def add_person():
    person={}
    name=input("Enter your Name: ")
    person['name']=(name)
    age=input("Enter your Age: ")
    person['age']=age
    email_id=input("Enter your E-mail ID: ")
    person['email-ID']=email_id
    
    people.append(person)
    
def delete_person(people):
    for index, person in enumerate(people):
        print(f"{index + 1} : {person['name']} | {person['age']} | {person['Email-ID']}")
        
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

def search_person(people):
    search_name=input("Enter the name of the person you want to search: ").capitalize()
    result=[]
    for person in people:
        if search_name == person["name"]:
            result.append(person)
    if len(result)==0:
        print("Name not found")
    else:
        print(result)
        

print("Hi, WELCOME to the Contact Management System")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]
   
while True:
    # size=len(people)
    print(f"Contact list size is: {len(people)}")
    action=input("Do you want to 'VIEW', 'ADD', 'DELETE', 'SEARCH' a person, or Enter 'q' to exit: ").lower()
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
    elif action=='q':
        break
    else:
        print("Invalid response, try again")
    
with open("contacts.json", "w") as f:
    json.dump({"contacts": people},f)

# print(people)