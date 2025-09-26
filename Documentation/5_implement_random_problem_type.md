# 5 Implement Random Problem Type

## Topics Covered

- Random and the choice method
- split method

## Actions

In order to pick a random problem type we are going to have to leverage two built in methods with python. The first is split. Split allows use to break strings up into objects in a list based on a delimiter. In this example we are using | to break up our string. The second method comes from the random module. the module itself has many power tools but the one we are interested in is choice(). Choice lets us pick a random value from a list. This is exactly what we need to get our program to work as expected. 

```python
  import random
  
  problem_types = "add|sub|mult|div".split("|")
  problem_type = random.choice(problem_types)
```

## Resources

[random](https://docs.python.org/3/library/random.html)
[random.choice()](https://docs.python.org/3/library/random.html#random.choice)
[split()](https://docs.python.org/3/library/stdtypes.html#str.split)