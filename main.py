secure=(('A','@'),('I','!'),('H','#'),('S','$'),(" and ",'&'),(" ",''),('l',"|"))
#function to replace the password according to given above secure touple
def reppass(password):
    #getting the element to replace fromsecuer -
    for a,b in secure:
        password=password.replace(a,b)
    return password

password=input("enter your password : ")
pass2=reppass(password.upper())
print(f"your secured password is : {pass2}")