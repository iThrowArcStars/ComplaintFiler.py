# By Austin Uhl, modified by Jason Pelkey

class Person():
    
    def __init__(self, name, age = None, complaint = None):
        """
        The constructor for the Person class
        
        Args:
            name (String): The name of the user filing the complaint
            age (int): The age of the user
            complaint (String): The complaint of the user
        """
        
        self.name = name
        self.age = age
        self.complaint = complaint
    
    #class methods
    def get_age(self):
        """
        Asks the user for their age.  Only allows numbers to be returned
        
        Returns:
            int: The age the user inputs
        """
        while True:
            try:
                user_age = int(input("Enter your age: "))
            except ValueError:
                print("Invalid input, please try again. ")
                continue
            break
        return user_age
    
    def get_complaint(self):
        """
        Asks the user to input their complaint
        
        Returns:
            String: The complaint the user typed
        """
        user_complaint = input("Enter complaint: ")
        return user_complaint
        
    def set_age(self, age):
        """ 
        Sets the age of the person based on the input paramater
        
        Args:
            age (int): The age to set the Person object to be
        """
        self.age = age
        
    def set_complaint(self, complaint):
        """
        Sets the complaint of the person based on the input paramater
        
        Args:
            complaint (String): The complaint of the person
        """
        self.complaint = complaint
    
    def __str__(self):
        return (self.name + ", age " + str(self.age) 
               + ", reports a complaint: " + self.complaint)

def get_name():
    """
    Asks the user for their name
    
    Returns:
        String: The name given by the user
    """
        user_name = input("Enter your name: ")
        return user_name

def create_person(people_data):
    """
    Asks the user for their name, then creates a Person object
    with said name.  Then we ask for the user's age and complaint,
    which we will also add to the Person object.
    
    Args:
        people_data (Dictionary): The dictionary to store the newly created 
                                  Person object into
    
    Returns:
        String: The name given by the user
    """
    
    # Get a name to call the user by
    user_name = get_name()
    
    # Create the person to store their data
    person_obj        = Person(user_name)
    
    # Store the person object into the people dictionary
    people_data[user_name] = person_obj
    
    # Get the person's age and complaint
    person_age        = person_obj.get_age()
    person_complaint  = person_obj.get_complaint()
    
    # Set the person's age and complaint to the Person object
    person_obj.set_age(person_age)
    person_obj.set_complaint(person_complaint)
    
    # Returns the name that the user gave for the Person complaint
    return user_name
    
def print_all_complaints(person_dict):
    """
    Prints all complaints from a given dictionary
    
    Args:
        person_dict (Dictionary[Person object]): The dictionary of Person 
                                                 objects to print from
    """
    
    dict_keys = list(person_dict.keys())
    
    # Prints every value in the dictionary
    for i in range(len(dict_keys)):
        key = dict_keys[i]
        person_object = person_dict[key]
        print(person_object)

def main():
    """
    Asks the user if they are making a complaint.
    If yes, use the method create_person().
    Else, print 'Have a good day!'.
    """
    
    # Creates a dictionary to store Person objects
    people = {}
    
    # Ask the user if they would like to make a complaint
    hasComplaint = input("Are you making a complaint? (Yes/No) ").lower()
    
    # If yes, then activate the complaint filer
    if hasComplaint == "yes":
        person = create_person(people)
        print_all_complaints(people)
    else: # Otherwise, do nothing
        pass
    
# CALL MAIN
if __name__ == "__main__":
    main()