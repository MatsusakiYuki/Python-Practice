#Author: Anni Li,
#Student ID: 30269776
#Start Date: Apr 5
#Last Modification date: Apr 12
#Description:
#This menu aims to collect inputs of Fandom Sccore, Hobbies Score and Sports Score from user input.
#

reco=list()
counter=0
while counter < 3:
    print("Welcome, here's the Main Menu! Please start with any one of the scores.")

    print("Please choose from: 1.Fandom Score, 2.Hobbies Score and 3.Sports Score.")
    choice = input()
    if str(choice).isdigit()== False or str(choice).isdecimal() == False:      #Check if the input is integer
        print("Please enter an integer.")
        choice = input()

    cho = int(choice)
    if cho < 1 or cho > 3:
        print("Please choose between 1 and 3.")  # value check for choice
        choice = input()


    # Prompt a user to enter the input for Fandom Score
    elif cho == 1:
        print("Please enter your Fandom Score")
        FandomScore = int(input())  # Pop out input and get input number
        if str(FandomScore).isdigit() == False or str(FandomScore).isdecimal() == False:  # Check if the input is integer
            print("Please enter an integer.")
            FandomScore = input()


        # Check value of the Fandom Score is positive integer
        if int(FandomScore) <= 0:
            print("Please enter a positive integer.")
            FandomScore = input()

        else:
            print ("Your Fandom Score is " + str(FandomScore) + ".")  # Print Fandom Score
            counter+=1
            reco.append(1)

    elif cho == 2:  # Prompt a user to enter the input for Hobbies Score
        print("Please enter your Hobbies Score on a weekly basis.")
        HobbiesScore = input()
        if str(HobbiesScore).isdigit() == False or str(HobbiesScore).isdecimal() == False:  # Check if the input is integer
            print("Please enter an integer.")
            HobbiesScore = input()

        # Value check for Hobbies Score
        if int(HobbiesScore) <= 0:  # check value is positive
            print("Please enter a positive multiple of 4")
            HobbiesScore = input()

        elif int(HobbiesScore) % 4 != 0:  # check value is the multiple of 4
            print("Please enter an integer at the multiple of 4.")
            HobbiesScore = input()

        else:
            print("Your Hobbies Score is " + str(HobbiesScore) + ".")  # Print Hobbies Score
            counter += 1
            reco.append(2)

    # Prompt a user to enter the input for Sports Score
    elif cho == 3:
        print("Please enter number of sports items you play with.")
        SportsNum = input()
        if str(SportsNum).isdigit() == False or str(SportsNum).isdecimal() == False:  # Check if the input is integer
            print("Please enter an integer.")
            SportsNum = input()

        # Value check for Sports Score
        if int(SportsNum) <= 0:  # check value to be positive
            print("please enter a positive number.")
            SportsNum = input()
        else:
            print("Your Sports Score is " + str(SportsNum) + ".")  # Print Hobbies Score
            counter += 1
            reco.append(3)

# check if all scores are entered by user
if len(reco)==3:
    i=0
    for int in reco:
        if 1 in reco:       # check if Fandom Score is entered
           i += 1
        else:
            print("Error in Fandom Score")      # report error if Fandom Score is not done

        if 2 in reco:       # check if Fandom Score is entered
            i += 1
        else:
            print("Error in Hobbies Score")     # report error if Hobbies Score is not done

        if 3 in reco:       # check if Sports Score is entered
            i += 1
        else:
            print("Error in Sports Score")     # report error if Sports Score is not done
        break




nerdscore=()  #calculate nerd score
print ("The Nerd Score is " + str(nerdscore) + ".")