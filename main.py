"""Create a program that can generate random math problems. The problems should include addition, subtraction, multiplication and division. The user should be able to choose what type of questions are returned and the amount of problems.

Ensure the program can handle common errors like the user inputting incorrect values.
"""

print("Welcome to MPG!")

problem_types = input("What type of problems do you want to generate? (add|sub|mult|div): ")
num_problems = int(input("How many problems should be created?: "))

print(f"Generating problems types {problem_types}...")
print(f"Generating {num_problems} problems...")

for i in range(0, num_problems):
  print(f"Creating problem {i+1}...")
  
  if "add" in problem_types:
    print("->addition problem")
    
  if "sub" in problem_types:
    print("->subtraction problem")
    
  if "mult" in problem_types:
    print("->multiplication problem")
    
  if "div" in problem_types:
    print("->division problem")

print("Complete!")