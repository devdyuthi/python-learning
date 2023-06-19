
cmd = ""
while cmd.lower() != "quit":
    cmd = input(">").lower()
    if cmd == "help":
        print("""
              start - to start the car 
              stop - to stop the car 
              quit - to exit
              
              """)
    elif cmd == "start":
        print("Car Started, ready to go!")
    elif cmd == "stop":
        print("Car stopped.....")
    else:
        print("I don't understand...")