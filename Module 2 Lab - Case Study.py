"""
Name: Iteoluwakiisi George Olaniyan
File Name: Module 2 Lab - Case Study
Description: This program accepts student names and GPAs to determine if the student qualifies
for either the Dean's List or the Honor Roll based on their GPA. The program will
continue to process student records until the user enters 'ZZZ' as the last name.

""" 

while True:
        last_name = input ("Enter last name( or enter ZZZ to quit): ") # Get student's last name
        if last_name == 'ZZZ': # Check if the last name entered is ZZZ so as to quit the program
                print("Exiting program...")
                break
        first_name = input ("Enter first name(or enter ZZZ to quit): ") # Get student's first name
        while True: # Get the student's gpa and making sure it is a valid input
            try:
                    gpa = float (input ("Enter gpa: "))
                    break
            except ValueError:
                   print("Invalid input. Enter a number")

        # Determine if the student qualifies for the Dean's list or Honor Roll or neither
        if gpa >= 3.5:
               print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
               print(f"{first_name}{last_name} has made the Honor Roll.")
        else:
               print(f"{first_name}{last_name} did not qualify for the Dean's List or Honor Roll.")
                             