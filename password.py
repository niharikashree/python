#TO CHECK FOR CORRECT PASSWORD AND PRINT LOGGED IN OR BLOCKED
actualpassword=2387
n=3
for i in range(0,3):
    password=input()
    if password==actualpassword:
            print("successfully logged in")
            break
    else:
        if n==1:
            print("your account gets blocked, try again later after 24 hours")
        else:
            print("incorrect password, you are left with ",n-1,"attempts")
            n=n-1
