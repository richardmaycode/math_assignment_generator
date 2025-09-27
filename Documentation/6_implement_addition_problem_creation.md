# 6 Implement Addition Problem Creation

## Topics Covered

- Using Random to create random numbers
- Using f-strings in python

## Actions
  Now that we can determine which problem the program will generate it's time to actually create the problem. We will start with the easiest which is addition. With addition we only need to create two random numbers and print them out with some decoration text to achieve our result. 
  
  ```python
    print(f"{random.randomint(1, 100)} + {random.randomint(1, 100)} = ______")
  ```

## Resources

[Random randint documentation](https://docs.python.org/3/library/random.html#random.randint)
[F-Strings](https://www.w3schools.com/python/python_string_formatting.asp)