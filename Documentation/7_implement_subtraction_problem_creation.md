# 7 Implement Subtraction Problem Creation

## Topics Covered

- min() and max() methods

## Actions

When creating our subtraction problems there is only one consideration; we should not create a problem that results in a negative number. In order to meet this requirement we will store our randomly generated numbers in variables named `num_1` and `num_2` then when we go to print the problem out we will make sure the highest number appears first and the lower number is second. We accomplish this using `min()` and `max()`. These are both methods on the integer class. `min()` returns the smallest number and `max()` returns the highest number. 

```python
  num_1 = random.randint(1, 100)
  num_2 = random.randint(1, 100)
  
  print(f"{max(num_1, num_2")} - {min(num_1, num_2)} = ______")
```

## Resources

[Creating Variables](https://www.w3schools.com/python/python_variables.asp)
[min() funtion](https://docs.python.org/3/library/functions.html#min)
[max() function](https://docs.python.org/3/library/functions.html#max)