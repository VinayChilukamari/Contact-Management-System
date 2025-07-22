
# Project: Contact Management System ~ project idea credit -tech with tim

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
            number=int(input(f"\nEnter the number of the person you want to {text}: "))
            if number<=0 or number>len(people):
                print("\nInvalid number, index out range")
            else:
                break
        except Exception as e:
            print("\nInvalid number, enter an integer value")

    return number

def add_person():# this function allows user to add new person to contacts.json file.
    person={}
    name=input("Enter your Name: ").strip()
    person['name']=(name)
    age=input("Enter your Age: ").strip()
    person['age']=age
    email_id=input("Enter your E-mail ID: ").strip()
    person['email-ID']=email_id
    
    people.append(person)
    
    json_dump()
    
def delete_person(people):# this function allows user to delete specified person from contacts.json file.
    display_contacts()
        
    if len(people)==0:
        print("\nContact list is empty")
    else:
        number=index_num_inp('delete') # function to get the index number of the list to delete
        people.pop(number-1)
    json_dump()

def search_person(people):# this functions allows user to search the person from contacts.json file.
    while True:
        result=[]
        search_by=input("\nDo you want to search by 'NAME', 'AGE', 'EMAIL-ID'? or enter 'q' to exit: ").lower()
        if search_by=='name':
            search_name=input("\nDo you want to search by 'FIRST NAME', 'LAST NAME', or 'FULL NAME'? (first/last/full): ").lower()
            if search_name=='first name' or search_name=='first':
                first_name=input("\nEnter the 'first name' of the person you want to search: ").strip()
                for person in people:
                    if first_name == person["name"][0:len(first_name)]:
                        result.append(person)
                break
            elif search_name =='last name' or search_name=='last':
                last_name=input("\nEnter the 'last name' of the person you want to search: ").strip()
                # print(last_name)
                for person in people:
                    if last_name == person["name"][-len(last_name):]:
                        result.append(person)
                break
            elif search_name =='full name' or search_name=='full':
                last_name=input("\nEnter the 'full name' of the person you want to search: ").strip()
                for person in people:
                    if last_name == person["name"]:
                        result.append(person)
                break
            else:
                print("\nInvalid search")
        elif search_by=='age':
            age_inp=input("\nEnter the 'age' of the person you want to search: ").strip()
            for person in people:
                if age_inp==person['age']:
                    result.append(person)
            break
        elif search_by=='email-id':
            email_inp=input("\nEnter the 'email-ID' of the person you want to search: ").strip()
            for person in people:
                if email_inp==person['email-ID']:
                    result.append(person)
            break
            
        elif search_by =='q':
            break
        else:
            print("\nInvalid search")
            
        
    if len(result)==0:
        print("\nPerson not found.\nNote: search is case-sensitive")
    else:
        for i in result:
            print('\n',i,'\n',sep='')
            
def change(people):# this functions allows user to change persos's attribute from contacts.json file.
    display_contacts()
    number=index_num_inp('change')
    # print(number)
    for person in people:
        change_index=number-1
        if change_index==people.index(person):
            while True:
                change_inp=input("\nSpecify what do you want to change? 'NAME', 'AGE', or 'EMAIL-ID'?: ").lower()
                if change_inp=='name':
                    o_name=people[change_index]['name']
                    u_name=''
                    change_by=input("\nDo you want to change by 'FIRST NAME', 'LAST NAME', or 'FULL NAME'? (first/last/full): ").lower()
                    if change_by=='first name' or change_by=='first':
                        update=o_name.split()
                        update.remove(update[0])
                        update.insert(0,input("\nEnter the updated name: ").strip())
                        u_name=' '.join(update)
                        people[change_index]['name']=u_name
                        json_dump()
                        print("\nFirst name updated")
                        break
                    elif change_by=='last name' or change_by=='last':
                        
                        update=o_name.split()
                        if len(update)==1:
                            print("\nLast name does not exist, please change in full name")
                            break
                        else:
                            update.remove(update[1])
                            update.insert(1,input("\nEnter the updated name: ").strip())
                            u_name=' '.join(update)
                            people[change_index]['name']=u_name
                            json_dump()
                            print("\nLast name updated")
                            break
                    elif change_by=='full name' or change_by=='full':
                        u_name=input("\nEnter the updated name: ").strip()
                        people[change_index]['name']=u_name
                        json_dump()
                        print("\nName updated")
                        break
                    else:
                        print("Invalid input")
                        
                    
                elif change_inp=='age':
                    people[change_index]['age']=input("\nEnter the updated age: ").strip()
                    json_dump()
                    print("\nAge updated")
                    break
                    
                elif change_inp=='email-id':
                    people[change_index]['email-ID']=input("\nEnter the updated email-ID: ").strip()
                    json_dump()
                    print("\nEmail-ID updated")
                    break
                else:
                    print("\nInvalid input, try again")
                
        

print("Hi, WELCOME to the Contact Management System")

people= json_read()
# print(people)
   
while True:
    print(f"\nContact list size is: {len(people)}")
    action=input("\nDo you want to 'VIEW', 'ADD', 'CHANGE', 'DELETE', 'SEARCH' a person, or Enter 'q' to exit: ").lower()
    if action=='add':
        add_person()
        print("\nPerson added!")
    elif action=='delete':
        delete_person(people)
        print("\nPerson deleted!")
    elif action=='search':
        search_person(people)
    elif action=='view':
        display_contacts()
    elif action=='change':
        change(people)
    elif action=='q':
        break
    else:
        print("\nInvalid response, try again")
    