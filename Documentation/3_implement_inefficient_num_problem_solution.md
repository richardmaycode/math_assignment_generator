# 3 Implement Inefficient num_problem Solution

## Topics Covered

- Comparision Operators
- If Statement

## Actions

Now that we have a way to get the request from the user we have to do something with it. 

we will attempt to process the request for a number of problems. We can use an if statement to see if a problem should be printed out but we will quickily discover that this is inefficient. We would have to write an if statement for every possibility. This would result in us either limiting the number of problems or having a problem with thousands of repeated lines of code. 

```python
  if num_problem == 1:
    # do something
  
  elif num_problem == 2:
    # do something
  
  else:
    print("This is too many problems")
```

## resources

[Comparision Operators (Python)](https://www.w3schools.com/python/python_operators.asp)
[If Statement](https://docs.python.org/3/reference/compound_stmts.html#if)