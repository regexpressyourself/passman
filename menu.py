def welcomeMessage():
    print("\n\n")
    print("##################################################")
    print("# Welcome to Passman!")
    print("##################################################\n\n")

def showMenu():
    prompt = "What do you want to do?\n\n" \
    + "(1) List all services\n" \
    + "(2) Add a new service\n" \
    + "(3) Remove an existing service\n" \
    + "(4) Edit an existing service\n" \
    + "(5) Get password for a service\n" \
    + "(6) Get username for a service\n" \
    + "(7) get URL for a service\n\n"

    option = getUserInput(prompt)
    if option =="1":
        listServicesPrompt()
    elif option =="2":
        addServicePrompt()
    elif option =="3":
        removeServicePrompt()
    elif option =="4":
        editServicePrompt()
    elif option =="5":
        getPassPrompt()
    elif option =="6":
        getNamePrompt()
    elif option =="7":
        getUrlPrompt()
    else:
        print("Didn't get that...\n")
        showMenu()


