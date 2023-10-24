# Print title of story
print(" ~ Tales from the Cryptic Code ~")
print(" ( A work of fiction )")
print()
print()
#Present the story
print("You are a programmer in the year 2025, and you're trying to be the best programmer of all. ")
print()
#Present user with story options
print()
print("You decide to go on a journey in NGC City to earn your glory")
print()
print("You are outside the city walls and see 3 people to ask for help:")
print()
print(" A. The town janitor, who has a broom")
print(" B. The town chef, who has a measuring cup")
print(" C. The software engineer, who needs a programmer")
print()
print("Who will you ask for help? Please select option 'A' - 'C' ")
#Inform user to select an option
answer = input(" Please enter 'A' - 'C': ")
# Print choice based on answer
if(answer == 'A'):
  
 #Show Janitor's story 

    
  print()
  print("You meet with the janitor, looking for a magical broom ")
  print("He tells you that he has a broom in his closet")
  print("You choose to search for it in:")
  print(" 1. The Garden")
  print(" 2. The Library")
  print(" 3. The Utility Closet")
  print()
  answer = input( "Please select option '1' - '3': ")
  print()
if answer == '1' or answer == '2':
  #Show user fail option
  print("You searched and searched but never found the broom.")
  print("As a result, you were fired from the company.")
  print(" ~ The End ~")
if answer == '3':
  #Show user successful option
  print("After searching the whole building, you find the magic broom in the utility closet.")
  print("The janitor is happy and gives you a free house cleaning.")
  print()
  print(" ~ The End ~")

if(answer == 'B'):
  
 #Show Chef's story 
  print()
  print("You meet with the chef who needs measuring cups")
  print("He tells you to solve an equation to find the cups")
  print("The equation is: 4tsp - 2tsp + 1tsp = ?")
  print()
  answer = input( "Please enter the number of teaspoons needed: ")
  print()
  if answer == '3':
    #Show user successful option
    print("You solved the equation and found the cups.")
    print("The chef is happy and gives you free baked goods for life.")
    print()
    print(" ~ The End ~")
  if answer != '3':
    #Show user fail option
    print("That is the wrong answer.")
    print("The chef punishes you by making you his dishwasher for life.")
    print()
    print(" ~ The End ~")
    print()

    
if(answer == 'C'):
  
 #Show Programmer's story
      print()
      print("You chose to meet with the Software Engineer who is in need of a top programmer")
      print("He asks you the correct language to use for the 'function' option")
      print()  
      print("A. #24 ")
      print("B. answer ")
      print("C. 'f'")
  
      answer = input( "Please select option 'A' - 'C': ")
      print()
      if answer == 'A' or answer == 'B':
        #Show user fail option
        print("You chose the wrong answer.")
        print("The Software Engineer tells all companies not to never hire you.")
        print()
        print(" ~ The End ~")
      if answer == 'C':
        #Show user successful option
        print("Congratulations! You chose the correct answer.")
        print("The Software Engineer is happy and gives you the top programmer job.")
        print()
        print(" ~ The End ~")
      
  
  
  








  





  
 






