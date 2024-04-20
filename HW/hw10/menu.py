from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ") # keeps looping through until 6 is chosen as the break number
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                try: # try and except block used so only the user tells the code when to stop
                    name = input("Enter the customer's name: ")
                    time = input("Enter the reservation time (HH:MM): ")
                    self.waitlist.add_customer(name, time) # call to add customer 
                    print (f"{name} has been added to the waitlist at {time}")
                except RuntimeError: # exception for when an invalid time is input
                    print("The input time is not a valid time (HH:MM)")

            elif choice == "2":
                #TODO"""Seat the next customer"""
                try: # try and except block used so only the user tells the code when to stop
                    seated = self.waitlist.seat_customer() # call to seat customer 
                    print (f"Seated customer: {seated.name}, reservation time: {seated.time}")
                except RuntimeError: # exception for when there is no one on the waitlist
                    print("The waitlist is empty")

            elif choice == "3":
                try: # try and except block used so only the user tells the code when to stop
                #TODO"""Change the time of a customer's reservation"""
                    name = input("Enter the customers name: ")
                    newtime = input("Enter the new reservation time (HH:MM): ")
                    print(self.waitlist.change_reservation(name, newtime)) # call to change reservation 
                except RuntimeError: # exception for when customer is not in list 
                    print("Customer is not in list")
                except KeyError: # exceptino for when input time is invalid 
                    print("The input time is not a valid time (HH:MM)")

            elif choice == "4":
                #TODO"""Peek at the next customer"""
                try:
                    peeked = self.waitlist.peek()
                    name = peeked.name
                    time = peeked.time
                    print(f"The next customer on the waitlist is: {name}, reservation time: {time}") # prints out the next customer on the waiting list according to peak
                except:
                    print("The waitlist is empty")
                    
            elif choice == "5":
                #TODO"""Print the waitlist"""
                print(self.waitlist.print_reservation_list()) # call to print reservation list

            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!") # breaks the loop only when the user wants to stop
                break
            else:
                print("Invalid choice. Try again.") # if a number not in the ran 1-6 is chosen nothing happens and this is printed
    
s = Menu()
s.run()

