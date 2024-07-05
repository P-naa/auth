savedusername = "name"
savedpassword = "passcode"
numberoftries = 3
 
while numberoftries !=0 :
    usernameinput = input("Please enter your username")
    passwordinput = input("Please enter ypur password")

    if (username==savedusername) and (passwordinput==savedpassword) :
        print(f"Welcome {savedusername}")
        break
    else:
        print("sorry please try again")
        numberoftries = numberoftries - 1
print("Please contact your administrator")