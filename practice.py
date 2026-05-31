"""
Git and GitHub Practice File
Use this script to practice branching, committing, pushing, and merging.
"""



def add_numbers(a, b):
    # TODO: Practice making a change here (e.g., return a + b)
    passdef welcome_message():
    print("Welcome to your Git/GitHub Practice Session!")
    print("--------------------------------------------")

def subtract_numbers(a, b):
    return a - b

def main():
    welcome_message()
    
    # Test your functions
    num1 = 10
    num2 = 5
    
    print(f"Subtracting {num2} from {num1}: {subtract_numbers(num1, num2)}")
    # Uncomment the line below once you implement add_numbers
    # print(f"Adding {num1} and {num2}: {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
def add_numbers(a, b):
<<<<<<< HEAD
   return a + b
def welcome_message():
    print("Welcome to your Git/GitHub Practice Session!")
    print("--------------------------------------------")
=======
    return a + b
>>>>>>> parent of e8d81b0 (rebasetesting)
