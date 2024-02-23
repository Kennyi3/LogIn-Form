import sys
import random

# Define the leaderboard as a list of dictionaries
leaderboard = []

def home():
    while True:
        # Number of lives the user has
        lives = 3
        user_name = input("Enter your name: ")  # Collect the user's name

        # Define level-specific scores
        level_scores = {
            "Easy": 0,
            "Moderate": 0,
            "Hard": 0,
            "Extreme": 0
        }

        # Questions and Multiple-Choice Answer for Easy
        easy_data =  [
    ("\nWhat is the most basic data type in Python?", ["a) int", "b) str", "c) float", "d) list"], "a"),
    ("\nWhat does 'print()' function do in Python?", ["a) takes a picture", "b) prints output to the console", "c) sends an email", "d) plays music"], "b"),
    ("\nWhat is the result of 2 + 2 in Python?", ["a) 3", "b) 5", "c) 4", "d) 6"], "c"),
    ("\nHow do you start a single-line comment in Python?", ["a) /*", "b) //", "c) #", "d) <!--"], "c"),
    ("\nWhich operator is used for exponentiation in Python?", ["a) ^", "b) **", "c) //", "d) %"], "b"),
    ("\nWhat is a variable in programming?", ["a) a container for storing data", "b) a type of food", "c) a programming language", "d) a person's name"], "a"),
    ("\nWhat is a for loop used for in Python?", ["a) making coffee", "b) washing dishes", "c) iterating over a sequence", "d) solving equations"], "c"),
    ("\nWhat is the difference between '==' and '!=' operators in Python?", ["a) '==' checks for equality, '!=' checks for inequality", "b) '==' checks for inequality, '!=' checks for equality", "c) They are the same.", "d) '==' checks for greater than, '!=' checks for less than"], "a"),
    ("\nWhat is a list in Python?", ["a) a list of tasks", "b) an ordered collection of items", "c) a mathematical equation", "d) a type of bug"], "b"),
    ("\nHow do you define a function in Python?", ["a) using the 'function' keyword", "b) using the 'define' keyword", "c) using the 'func' keyword", "d) using the 'def' keyword"], "d")
]

        # Questions and Multiple-Choice Answer for Moderate
        moderate_data = [
    ("\nWhat is the purpose of 'if' statements in Python?", ["a) To define a function", "b) To perform conditional execution", "c) To declare a variable", "d) To create a list"], "b"),
    ("\nHow do you write a 'for' loop in Python?", ["a) for (i = 0; i < 5; i++)", "b) for i in range(5)", "c) loop (i = 0; i < 5)", "d) iterate 5 times"], "b"),
    ("\nWhat is the result of 4 / 2 in Python?", ["a) 1.0", "b) 2", "c) 4", "d) 0.5"], "b"),
    ("\nHow can you add a comment in Python?", ["a) // This is a comment", "b) /* This is a comment */", "c) # This is a comment", "d) <!-- This is a comment -->"], "c"),
    ("\nWhich data type is used for a single character in Python?", ["a) char", "b) character", "c) str", "d) single"], "c"),
    ("\nWhat does the 'len()' function do in Python?", ["a) Returns the total number of items in a list", "b) Finds the length of a string", "c) Calculates the product of a list", "d) Determines the largest number in a list"], "a"),
    ("\nHow do you define a function in Python?", ["a) function myFunction() { }", "b) func myFunction():", "c) def myFunction():", "d) define myFunction():"], "c"),
    ("\nWhat is the difference between '==' and '!=' operators in Python?", ["a) '==' checks for equality, '!=' checks for inequality", "b) '==' checks for inequality, '!=' checks for equality", "c) They are the same.", "d) '==' checks for greater than, '!=' checks for less than"], "a"),
    ("\nWhat is a tuple in Python?", ["a) An ordered collection of items", "b) A data type for storing text", "c) A loop that repeats a specific number of times", "d) A type of bug"], "a"),
    ("\nWhat is the output of '2' + '3' in Python?", ["a) 5", "b) 23", "c) '23'", "d) Error"], "c")
]

        # Questions and Multiple-Choice Answer for Hard
        hard_data =  [
    ("\nExplain the concept of 'recursion' in programming.", ["a) A function that calls itself", "b) A loop that repeats indefinitely", "c) A type of data structure", "d) A database management system"], "a"),
    ("\nWhat is the purpose of 'try' and 'except' in exception handling?", ["a) Handling file operations", "b) Handling keyboard input", "c) Handling exceptions and errors", "d) Handling network connections"], "c"),
    ("\nWhat is object-oriented programming (OOP) and how does it relate to Python?", ["a) A programming language", "b) A coding style", "c) A programming paradigm that uses objects and classes; Python supports OOP", "d) A Python library"], "c"),
    ("\nWhat are the principles of clean code and why are they important?", ["a) Optimization and speed", "b) Readability, maintainability, and collaboration; important for code quality", "c) Code length and complexity", "d) Use of the latest programming tools"], "b"),
    ("\nDescribe the use of 'decorators' in Python.", ["a) Adding furniture to a room", "b) Adding comments to code", "c) Functions that modify other functions", "d) A Python design pattern"], "c"),
    ("\nWhat is the purpose of 'sys.argv' in Python?", ["a) A mathematical function", "b) A module for system-level operations", "c) A command-line argument list", "d) A built-in Python function"], "c"),
    ("\nWhat is the 'self' parameter in Python methods?", ["a) It represents the first parameter of a function", "b) It is used to refer to the current instance of the class", "c) It is a reserved keyword", "d) It is used to access global variables"], "b"),
    ("\nWhat is an 'exception' in Python?", ["a) A syntax error", "b) An unwanted program output", "c) An error that occurs during program execution", "d) A type of data"], "c"),
    ("\nWhat is 'PEP 8' in Python?", ["a) A Python editor program", "b) A code testing tool", "c) The Python Enhancement Proposal that describes the style guide for writing clean code", "d) A Python data visualization library"], "c"),
    ("\nWhat is the purpose of the 'with' statement in Python?", ["a) To define a new class", "b) To create a list", "c) To simplify exception handling by encapsulating common preparation and cleanup tasks", "d) To declare a variable"], "c")
]

        # Questions and Multiple-Choice Answer for Extreme
        extreme_data = [
    ("\nWhat are lambda functions in Python and when are they used?", ["a) Long-term memory management", "b) Anonymous functions used for short, simple operations", "c) High-level programming languages", "d) Video game development"], "b"),
    ("\nExplain the Global Interpreter Lock (GIL) in Python.", ["a) A way to lock your computer", "b) A global code repository", "c) A mutex that allows only one thread to execute in CPython", "d) A debugging tool"], "c"),
    ("\nWhat is the purpose of the 'yield' keyword in Python?", ["a) Yielding control to another process", "b) Yielding a crop in a farming simulation game", "c) Used in generators to yield a value and save state", "d) A Python keyword for exiting a program"], "c"),
    ("\nDescribe the concept of 'Big O notation' in algorithm analysis.", ["a) A music notation system", "b) A way to measure the physical size of data", "c) A notation for analyzing the efficiency of algorithms", "d) A method for printing large text"], "c"),
    ("\nHow does Python manage memory and garbage collection?", ["a) Manually releasing memory", "b) Using a memory card", "c) Uses automatic memory management and a reference counting system", "d) Allocating memory using malloc"], "c"),
    ("\nWhat is 'asynchronous programming' in Python?", ["a) A way to run a program faster", "b) A coding style that uses only uppercase letters", "c) A programming technique that allows tasks to run concurrently without blocking the main program", "d) A form of data encryption"], "c"),
    ("\nWhat is the purpose of the 'map' function in Python?", ["a) To create a map of a geographic location", "b) To apply a given function to all items in an input list and return a new list", "c) To plot data on a graph", "d) To find directions between two points"], "b"),
    ("\nWhat is the 'Zen of Python'?", ["a) A popular Python book", "b) A Python programming framework", "c) A collection of software libraries", "d) A set of aphorisms that capture the design philosophy of Python"], "d"),
    ("\nWhat is 'type hinting' in Python?", ["a) A way to annotate code with comments", "b) A method for encrypting data", "c) A feature that allows you to add type information to function and variable declarations", "d) A way to check for syntax errors"], "c"),
    ("\nWhat is the purpose of 'pip' in Python?", ["a) A code editor for Python", "b) A tool for managing Python packages", "c) A Python programming language feature", "d) A way to print text to the console"], "b")
]


        completed_levels = []
        available_levels = {
            "1": ("Easy", easy_data),
            "2": ("Moderate", moderate_data),
            "3": ("Hard", hard_data),
            "4": ("Extreme", extreme_data)
        }

        while True:
            print("\nWelcome to our ITE 266 Quiz\nChoose an Intensity level you want: ")
            for level_num, (level_name, _) in available_levels.items():
                print(f"{level_num}. {level_name}")

            choice = input("Select an option (1/2/3/4): ")  # Removed option 5

            if choice in available_levels:
                level_name, level_data = available_levels[choice]
                lives = quiz(level_data, lives)
                completed_levels.append(level_name)
                level_scores[level_name] = len(completed_levels)
                del available_levels[choice]
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            if lives > 0:
                print("\nCongratulations,", user_name, "! You've completed all available levels.")
                print("Completed levels:", ", ".join(completed_levels))
            while True:
                play_again = input("\nDo you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    break  # Break the loop and continue the game
                elif play_again.lower() == "no":
                    # Add the user's name and scores to the leaderboard
                    leaderboard.append({"Name": user_name, **level_scores})
                    display_leaderboard(leaderboard)
                    sys.exit()
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
        else:
            while True:
                play_again = input("You've run out of lives. Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    break  # Break the loop and restart the game
                elif play_again.lower() == "no":
                    sys.exit()
                else:
                    print("Invalid choice. Please enter 'yes' or 'no.")

def quiz(questions, lives):
    correct_answers = 0

    # Shuffle the questions for this level
    random.shuffle(questions)

    for question, options, correct_answer in questions:
        print(question)
        for option in options:
            print(option)
        user_answer = input("Your answer (a/b/c/d): ")
        if is_answer_correct(user_answer, correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            lives -= 1
            if lives == 0:
                print("You don't have enough lives, Try again")
                break
    return lives

def is_answer_correct(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def display_leaderboard(leaderboard):
    # Sort the leaderboard by total score in descending order
    leaderboard.sort(key=lambda x: sum(x.values()), reverse=True)

    # Print the leaderboard with specified formatting
    print("\nLeaderboard:")
    print(f"{'Ranking':<10}{'Name':<20}{'Total Score':<15}{'Easy':<15}{'Moderate':<15}{'Hard':<15}{'Extreme':<15}")
    for i, player in enumerate(leaderboard, start=1):   
        print(f"{i:<10}{player['Name']:<20}{sum(player.values()):<15}{player['Easy']:<15}{player['Moderate']:<15}{player['Hard']:<15}{player['Extreme']:<15}")

home()