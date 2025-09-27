"""Create a program that can generate random math problems. The problems should include addition, subtraction, multiplication and division. The user should be able to choose what type of questions are returned and the amount of problems.

Ensure the program can handle common errors like the user inputting incorrect values.
"""
import random

print("Welcome to MPG!")

problem_types = input("What type of problems do you want to generate? (add|sub|mult|div): ").split("|")
num_problems = int(input("How many problems should be created?: "))

print(f"Generating problems types {problem_types}...")
print(f"Generating {num_problems} problems...")

for i in range(0, num_problems):
  print(f"Creating problem {i+1}...")
  
  problem_type = random.choice(problem_types)
  
  if "add" == problem_type:
    print(f"{random.randint(1, 100)} + {random.randint(1, 100)} = ______")
    
  if "sub" == problem_type:
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    print(f"{max(num_1, num_2)} - {min(num_1, num_2)} = ______")
    
  if "mult" == problem_type:
    print("->multiplication problem")
    
  if "div" == problem_type:
    print("->division problem")

print("Complete!")