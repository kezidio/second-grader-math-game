'''
Program:computer_assisted_functions.py.

Programmer: Kaweny Ezidio

Date: 10/02/2022

Description: Computer-assisted instruction (CAI) refers to the use of computers
in education. Write a program to help an elementary school student learn
multiplication, division, addition, and subtraction.

'''

# importing random function to be used bellow
import random

# program used: Iddle

# * PLEASE note that answer is is set to 2 decimal places

# Creating a function called get_operation
def get_operation():
#criating a variable 
    operation = 0
# criating a loop that will work for until the number -1 is inserted
    while(operation != -1):
# Prompting user to insert an operation number after the message
        operation = int(input("""\n1 = addition
2 = subtraction
3 = multiplication
4 = division \n
Enter the operation (1 to 4) or -1 to exit: """))
# Printing message when user enters -1       
        if(operation == -1):
            print("Thanks for playing!")
# Printing message when user enters any numbers different than 1 to 4.           
        elif(operation < 1 or operation > 4):
            print ("You did not enter a valid number, try again!")
        else:
          break
# ending the function call and returning the results        
    return operation

# Creating a function called create_question with parameter operation
def create_question(operation):
# declaring variables that will display random numbers for calculations
    number_1 = random.randint(1,20)
    number_2 = random.randint(1,20)
# declaring variables that will display question and compute operations
    question_text = 0
    question_answer = 0
    
# criating a condition to add numbers when user inputs number 1 in operation    
    if(operation == 1):
        question_text = "\nHow much is " + str(number_1) + " + " + str(number_2) + "?"
        question_answer = number_1 + number_2
# criating a condition to subtract numbers when user inserts number 2 in operation
    elif(operation == 2):
        question_text = "\nHow much is " + str(number_1) + " - " + str(number_2) + "?"
        question_answer = number_1 - number_2
# criating a condition to multiply numbers when user inserts number 3 in operation
    elif(operation == 3):
        question_text = "\nHow much is " + str(number_1) + " * " + str(number_2) + "?"
        question_answer = number_1 * number_2
# criating a condition to divide numbers when user inserts number 4 in operation        
    elif(operation == 4):
        question_text = "\nHow much is " + str(number_1) + " / " + str(number_2) + "?"
        question_answer = number_1 / number_2
# ending the function call and returning the results        
    return(question_text, question_answer)

# Creating a function called check_answer with parameters guess and answer
def check_answer(guess, answer):
    answer = float(format((answer),',.2f'))
    if(guess == answer):
        return True
    else:
        return False
    
# Creating a function called get_response with parameter is_correct
def get_response(is_correct):
    if(is_correct == True):
        return("\nCorrect, good work!")
    if(is_correct == False):
        return("\nIncorrect, please try again!")
    
# Creating a function main that will group all functions    
def main():
    operation = get_operation()
    (question, answer) = create_question(operation)
    if operation == -1:
      return
    print(question)
    guess = float(input("Enter your answer:"))
    is_correct = check_answer(guess, answer)
    print(get_response(is_correct))
    while(is_correct == False):
        guess = float(input("Enter your answer:"))
        is_correct = check_answer(guess, answer)
        print(get_response(is_correct))
    if(is_correct == True):
        main()
    
            
# Calling the main function
main()