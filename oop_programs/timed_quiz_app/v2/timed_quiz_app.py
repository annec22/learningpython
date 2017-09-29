import os

from quiz import Quiz


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    name = input("Please enter your name: ")
    clear_screen()
    print("Hi {}! Welcome to Timed Math Quiz App Version 2!".format(name))
    print("This game will measure how fast and accurate you can solve basic Math problems.")
    input("Press ENTER to continue...")


def get_quiz_preference():
    clear_screen()
    try:
        question_count = int(input("How many Math questions do you like to answer? "))
    except ValueError:
        print("Invalid value is given. Default value will be used. ")
        question_count = 0

    try:
        max_number = int(input("What is the highest number you want to solve? "))
    except ValueError:
        print("Invalid value is given. Default will be used. ")
        max_number = 0

    return question_count, max_number

def play_quiz():
    play = True
    while play:
        question_count, max_number = get_quiz_preference()
        new_quiz = Quiz(0,0)

        if  (not question_count) and (not max_number):
            new_quiz = Quiz()
        elif question_count and max_number:
            new_quiz = Quiz(question_count=question_count, max_num=max_number)
        else:
            new_quiz = Quiz(question_count=question_count) if question_count else Quiz(max_num=max_number)

        new_quiz.take_quiz()

        if input("Play again? <Enter> to play again, QUIT to exit: ").upper() == "QUIT":
            print("Bye now!")
            play = False
        else:
            clear_screen()

clear_screen()
welcome()
play_quiz()





