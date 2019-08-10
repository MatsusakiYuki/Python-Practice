#Author: Anni Li,
#Student ID: 30269776
#Start Date: Apr 6
#Last Modification date: Apr 12
#Description:
#This program is written to calculate an equation with given input. Firstly the three different scores are attributed to simpler variables.
#The variables are examined to be positive integers.And for Hobbies Score, the variable requires user input to be a multiple of 4, including 0
#Then the variables are proceeded into a complex formula Skill Equation to calculate a skill score.



# Functionality: cailculate the skill score by the equation
# x, y, z are inputs
def calculateSkillEquation(FandomScore, HobbiesScore, SportsNum):
	skillScore = 0  # intialize the output list
	
	# Please write your own program here
	x=FandomScore
	y=HobbiesScore
	z=SportsNum

	i=0
	while i<3:
		if isinstance(x,int) == False:		# Validation for Fandom Score,check if the number is an integer
			print("The input is float.Please enter a positive integer for Fandom Score.")
			x = input()

		elif int(x) <=0:		# Validation for Fandom Score to check if the number is positive
			print("Please enter a positive integer for Fandom Score.")
			x = input()

		else:
			i+=1

		if isinstance(y,int) == False:		# Validation for Hobbies Score,check if the number is an integer
			print("The input is float.Please enter a positive integer for Hobbies Score.")
			y = input()

		elif int(y) <= 0:  # Validation for Hobbies Score,check if the number is positive
			print("Please enter a positive multiple of 4")
			y = input()

		elif int(y) % 4 != 0:  # check value is the multiple of 4
			print("Please enter an integer at the multiple of 4.")
			y = input()
		else:
			i+=1

		if isinstance(z,int) == False:		# Validation for Sports Score,check if the number is an integer
			print("The input is float.Please enter a positive integer for Sports Score.")
			z = input()
		elif int(z)<= 0:  # Validation for SportsNum,check if the number is positive
			print("please enter a positive number for Sports Score.")
			z = input()
		else:
			i+=1

	if i == 3:
		skillScore = (42*(y**2)/(z+1))**(1/2)*x		# Execution of equation

	return skillScore


if __name__ == '__main__':
	FandomScore, HobbiesScore, SportsNum = 1, 4, 1  # the output should be 18.33030277982336


	print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))