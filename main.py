#Python test 
user_score = int(input("Enter your score: "))
max_score = 50

if user_score > max_score:
   print("Are you sure you entered the right score?")

percentage = (user_score / max_score) * 100

if user_score <= max_score:
  if percentage >= 90:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("A+")
  elif percentage >= 80:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("A")
  elif percentage >= 70:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("B")
  elif percentage >= 60:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("C")
  elif percentage >= 50:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("D")
  else:
    print("Your percentage is",round(percentage))
    print("Your grade is given below")
    print("U")
  
