class QuizApp:
    def __init__(self):
        self.lives = 3
        self.completed_levels = []
        self.current_question = 0

        self.easy_data = [
            ("What is the most basic data type in Python?", ["a) int", "b) str", "c) float", "d) list"], "a"),
            ("What does 'print()' function do in Python?", ["a) takes a picture", "b) prints output to the console", "c) sends an email", "d) plays music"], "b"),
            ("What is the result of 2 + 2 in Python?", ["a) 3", "b) 5", "c) 4", "d) 6"], "c"),
            ("How do you start a single-line comment in Python?", ["a) /*", "b) //", "c) #", "d) <!--"], "c"),
            ("Which operator is used for exponentiation in Python?", ["a) ^", "b) **", "c) //", "d) %"], "b")
        ]

        self.moderate_data = [
            ("What is a variable in programming?", ["a) a container for storing data", "b) a type of food", "c) a programming language", "d) a person's name"], "a"),
            ("What is a for loop used for in Python?", ["a) making coffee", "b) washing dishes", "c) iterating over a sequence", "d) solving equations"], "c"),
            ("What is the difference between '==' and '!=' operators in Python?", ["a) '==' checks for equality, '!=' checks for inequality", "b) '==' checks for inequality, '!=' checks for equality", "c) They are the same.", "d) '==' checks for greater than, '!=' checks for less than"], "a"),
            ("What is a list in Python?", ["a) a list of tasks", "b) an ordered collection of items", "c) a mathematical equation", "d) a type of bug"], "b"),
            ("How do you define a function in Python?", ["a) using the 'function' keyword", "b) using the 'define' keyword", "c) using the 'func' keyword", "d) using the 'def' keyword"], "d")
        ]

        self.hard_data = [
            ("Explain the concept of 'recursion' in programming.", ["a) A function that calls itself", "b) A loop that repeats indefinitely", "c) A type of data structure", "d) A database management system"], "a"),
            ("What is the purpose of 'try' and 'except' in exception handling?", ["a) Handling file operations", "b) Handling keyboard input", "c) Handling exceptions and errors", "d) Handling network connections"], "c"),
            ("What is object-oriented programming (OOP) and how does it relate to Python?", ["a) A programming language", "b) A coding style", "c) A programming paradigm that uses objects and classes; Python supports OOP", "d) A Python library"], "c"),
            ("What are the principles of clean code and why are they important?", ["a) Optimization and speed", "b) Readability, maintainability, and collaboration; important for code quality", "c) Code length and complexity", "d) Use of the latest programming tools"], "b"),
            ("Describe the use of 'decorators' in Python.", ["a) Adding furniture to a room", "b) Adding comments to code", "c) Functions that modify other functions", "d) A Python design pattern"], "c")
        ]

        self.extreme_data = [
            ("What are lambda functions in Python and when are they used?", ["a) Long-term memory management", "b) Anonymous functions used for short, simple operations", "c) High-level programming languages", "d) Video game development"], "b"),
            ("Explain the Global Interpreter Lock (GIL) in Python.", ["a) A way to lock your computer", "b) A global code repository", "c) A mutex that allows only one thread to execute in CPython", "d) A debugging tool"], "c"),
            ("What is the purpose of the 'yield' keyword in Python?", ["a) Yielding control to another process", "b) Yielding a crop in a farming simulation game", "c) Used in generators to yield a value and save state", "d) A Python keyword for exiting a program"], "c"),
            ("Describe the concept of 'Big O notation' in algorithm analysis.", ["a) A music notation system", "b) A way to measure the physical size of data", "c) A notation for analyzing the efficiency of algorithms", "d) A method for printing large text"], "c"),
            ("How does Python manage memory and garbage collection?", ["a) Manually releasing memory", "b) Using a memory card", "c) Uses automatic memory management and a reference counting system", "d) Allocating memory using malloc"], "c")
        ]

        self.questions = []

        self.load_data()

    def load_data(self):
        self.questions.extend(self.easy_data)
        self.questions.extend(self.moderate_data)
        self.questions.extend(self.hard_data)
        self.questions.extend(self.extreme_data)

    def load_next_question(self):
        if self.lives == 0:
            print("Game Over")
            return

        if self.questions:
            question, options, correct_answer = self.questions.pop(0)
            self.current_question += 1
            print(f"{self.current_question}. {question}")
            for i, option in enumerate(options):
                print(option)
        else:
            self.completed_levels.append("Level Name")  # Replace with the actual level name
            self.current_question = 0
            self.lives = 3
            print("Congratulations! You've completed the level!")

    def check_answer(self, user_answer):
        if user_answer is not None:
            correct_answer = self.correct_answers[self.current_question - 1]
            if user_answer == correct_answer:
                print("Correct")
            else:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over")
                else:
                    print(f"Incorrect. Lives remaining: {self.lives}")
        else:
            print("Invalid Answer. Please select an answer.")

if __name__ == "__main__":
    app = QuizApp()
    print("Choose a level:")
    print("1 - Easy level")
    print("2 - Moderate level")
    print("3 - Hard level")
    print("4 - Extreme level")

    level_choice = input("Enter the number of the level you want to play: ")

    if level_choice == "1":
        app.easy_data = [
            ("What is the most basic data type in Python?", ["a) int", "b) str", "c) float", "d) list"], "a"),
            ("What does 'print()' function do in Python?", ["a) takes a picture", "b) prints output to the console", "c) sends an email", "d) plays music"], "b"),
            ("What is the result of 2 + 2 in Python?", ["a) 3", "b) 5", "c) 4", "d) 6"], "c"),
            ("How do you start a single-line comment in Python?", ["a) /*", "b) //", "c) #", "d) <!--"], "c"),
            ("Which operator is used for exponentiation in Python?", ["a) ^", "b) **", "c) //", "d) %"], "b")
        ]
    elif level_choice == "2":
        app.moderate_data = [
            ("What is a variable in programming?", ["a) a container for storing data", "b) a type of food", "c) a programming language", "d) a person's name"], "a"),
            ("What is a for loop used for in Python?", ["a) making coffee", "b) washing dishes", "c) iterating over a sequence", "d) solving equations"], "c"),
            ("What is the difference between '==' and '!=' operators in Python?", ["a) '==' checks for equality, '!=' checks for inequality", "b) '==' checks for inequality, '!=' checks for equality", "c) They are the same.", "d) '==' checks for greater than, '!=' checks for less than"], "a"),
            ("What is a list in Python?", ["a) a list of tasks", "b) an ordered collection of items", "c) a mathematical equation", "d) a type of bug"], "b"),
            ("How do you define a function in Python?", ["a) using the 'function' keyword", "b) using the 'define' keyword", "c) using the 'func' keyword", "d) using the 'def' keyword"], "d")
        ]
    elif level_choice == "3":
        app.hard_data = [
            ("Explain the concept of 'recursion' in programming.", ["a) A function that calls itself", "b) A loop that repeats indefinitely", "c) A type of data structure", "d) A database management system"], "a"),
            ("What is the purpose of 'try' and 'except' in exception handling?", ["a) Handling file operations", "b) Handling keyboard input", "c) Handling exceptions and errors", "d) Handling network connections"], "c"),
            ("What is object-oriented programming (OOP) and how does it relate to Python?", ["a) A programming language", "b) A coding style", "c) A programming paradigm that uses objects and classes; Python supports OOP", "d) A Python library"], "c"),
            ("What are the principles of clean code and why are they important?", ["a) Optimization and speed", "b) Readability, maintainability, and collaboration; important for code quality", "c) Code length and complexity", "d) Use of the latest programming tools"], "b"),
            ("Describe the use of 'decorators' in Python.", ["a) Adding furniture to a room", "b) Adding comments to code", "c) Functions that modify other functions", "d) A Python design pattern"], "c")
        ]
    elif level_choice == "4":
        app.extreme_data = [
            ("What are lambda functions in Python and when are they used?", ["a) Long-term memory management", "b) Anonymous functions used for short, simple operations", "c) High-level programming languages", "d) Video game development"], "b"),
            ("Explain the Global Interpreter Lock (GIL) in Python.", ["a) A way to lock your computer", "b) A global code repository", "c) A mutex that allows only one thread to execute in CPython", "d) A debugging tool"], "c"),
            ("What is the purpose of the 'yield' keyword in Python?", ["a) Yielding control to another process", "b) Yielding a crop in a farming simulation game", "c) Used in generators to yield a value and save state", "d) A Python keyword for exiting a program"], "c"),
            ("Describe the concept of 'Big O notation' in algorithm analysis.", ["a) A music notation system", "b) A way to measure the physical size of data", "c) A notation for analyzing the efficiency of algorithms", "d) A method for printing large text"], "c"),
            ("How does Python manage memory and garbage collection?", ["a) Manually releasing memory", "b) Using a memory card", "c) Uses automatic memory management and a reference counting system", "d) Allocating memory using malloc"], "c")
        ]

    app.load_data()
    app.load_next_question()