contact_list = [ { "name" : "Rashmi" ,
                   "number" : "8797989821" ,
                   "email" : "rr@gmail.com" },
                 { "name" : "Saria" ,
                   "number" : "9897988245" ,
                   "email" : "ss@gmail.com" } ]


enter_a_choice=input("please enter 1 to find by name or 2 to find by number and 3 if you want to edit any of the numbers ")
if enter_a_choice=='1':
    get_name=input(" Enter a name ")
if get_name=="Rashmi":
    print(contact_list[0])
if get_name=="saria":
    print(contact_list[1])

if enter_a_choice=="2":
    get_number=input("enter a number")
if get_number=='8797989821':
    print(contact_list[0])
elif get_number==9897988245:
    print(contact_list[1])

if enter_a_choice=='3':
    name_to_edit=input("which number would you like to edit? ")
if name_to_edit=="rashmi":
    get_new_number=int(input("Enter the new number "))
    for d in contact_list:
        d.update((k, get_new_number) for k, v in d.items() if v == "8797989821")
elif name_to_edit=="saria":
    get_new_number=int(input("enter the new number "))
    for d in contact_list:
        d.update((k, get_new_number) for k, v in d.items() if v == "9897988245")
print(contact_list)




