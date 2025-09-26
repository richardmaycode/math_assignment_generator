"""Create a program that can generate random math problems. The problems should include addition, subtraction, multiplication and division. The user should be able to choose what type of questions are returned and the amount of problems.

Ensure the program can handle common errors like the user inputting incorrect values.
"""

print("Welcome to MPG!")

problem_types = input("What type of problems do you want to generate? (add|sub|mult|div): ")
num_problems = int(input("How many problems should be created?: "))

print(f"Generating problems types {problem_types}...")
print(f"Generating {num_problems} problems...")

if num_problems == 1:
  print("Creating problem 1...")

elif num_problems == 2:
  print("Creating problem 1...")
  print("Creating problem 2...")

else:
  print("too many problems requested...")

print("Complete!")