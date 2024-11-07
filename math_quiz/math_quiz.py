import random


def random_number(min, max):
    """
    Returns a random number between the 'min' and 'max' values. 
    """
    return random.randint(min, max)


def random_operator():
    """
    Selects a random operator from the list and returns the corresponding string.
    """
    return random.choice(['+', '-', '*'])


def operation(number1, number2, operator):
    """
    Creates an operation and returns the string representing the operation and its corresponding answer (int).
    """
    operation = f"{number1} {operator} {number2}"
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return operation, answer

def math_quiz():
    """
    Creates a math quiz game where the user answers math problems.
    """
    
    score = 0 #represents user's score in the game
    number_of_questions = 2 #represents number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):
        # Generate random numbers and an operator for the question
        number1 = random_number(1, 10); 
        number2 = random_number(1, 5); 
        operator = random_operator()

        # Create the operation text and generate the correct answer
        operation_text, answer = operation(number1, number2, operator)

        #Show the question to the user
        print(f"\nQuestion: {operation_text}")

        #Make sure the input is an int
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
            
        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

if __name__ == "__main__":
    math_quiz()