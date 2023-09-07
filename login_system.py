
thisdict={
    "username": ["ahmed","ali","amr"],
    "password": [1394,6078,9345]
}

login_username= input("please enter username: ")
if (login_username in thisdict["username"]):
    login_password= int(input("please enter your password: "))
    if (login_password in thisdict["password"]):
        print("welcome {}".format(login_username))
    else:
        print("the username and password are incorrect")
else:
  print("the username is incorrect")


