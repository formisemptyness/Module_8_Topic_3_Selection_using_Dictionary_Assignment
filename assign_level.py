'''
Program: assign_level.py
Author: Joshua M McGinley
Last Date Modified: 10/19/2022

You learned sequence structure, statements executed in order, then selection statements with if statements, then
looping statements. In some languages, there is a case selection statements, sometimes called switch/case.
In Python, you can write your own case statement using a function and a dictionary.
In this assignment you will implement a switch/case with a dictionary. You will assign points for attaining a level
in a video game. Levels are named N (for novice), B (for beginner), E (for experienced) and A (for advanced). For
novice, 50 points is assinged to get the player started. For attaining beginner, 150 points are recieved.
Experienced players receive 300 points while Advanced players 500.
In Module8 project

    Create a file assign_level.py
        Write switch_level() to assign points to a leve
            Include the cases outlined above
        Write main()
            call switch_level() for various levels and print the results

This is worth 10 points.

As a hint for those struggling:
Look at the above switch example and think through how it would compare to the previous dictionary example we saw:
a_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
And think through if you have an input 'user_input', how would we check and see if a_dict contains user_input?
'''

def switch_level(level):
    user_level = {'N': 50, 'B': 150, 'E': 300, 'A': 500}
    return user_level.get(level, 'You have failed!')

if __name__=='__main__':
    level = input('Enter you level: ')
    exp = switch_level(level)
    print(exp)

