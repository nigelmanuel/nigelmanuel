import random
import time
username = "admin"
userID = "173840293"
computer_name = "C-89208402"
computer_OS = "Windows XP"
  
random = random.randint(1,2)

if random == 1 :
    print("Login sucessfully done")
    time.sleep(1.5)
    print("Extracting data from computer...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(5)
    print("username: ", username)
    time.sleep(5)
    print("userID: ", userID)
    time.sleep(5)
    print("computer_name: ", computer_name)
    time.sleep(5)
    print("computer_OS: ", computer_OS)    
    ask1 = input("Do want to restart? (y/n)")
    if ask1 == "y":
        print ("error 404")
        print ("Restarting...")
        time.sleep(5)
        print("Cannot restart. Trying again. (1)")
        time.sleep(5)
        print("Cannot restart. Trying again. (2)")
        time.sleep(5)
        print("Cannot restart. Trying again. (3)")
        time.sleep(5)
        print("Cannot restart. Trying again. (4)")
        time.sleep(5)
        print("Cannot restart. Trying again. (5)")
        time.sleep(5)
        print("Please manually restart your computer")
    elif ask1 == "n":
        print("Shutting down...")
    else :
        print("Invalid")
else :
    print ("error 404")
    print ("Restarting...")
    time.sleep(5)
    print("Cannot restart. Trying again. (1)")
    time.sleep(5)
    print("Cannot restart. Trying again. (2)")
    time.sleep(5)
    print("Cannot restart. Trying again. (3)")
    time.sleep(5)
    print("Cannot restart. Trying again. (4)")
    time.sleep(5)
    print("Cannot restart. Trying again. (5)")
    time.sleep(5)
    print("Please manually restart your computer")
    
