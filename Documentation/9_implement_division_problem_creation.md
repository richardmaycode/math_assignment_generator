# 9 Implement Division Problem Creation

# Topics Covered

- No New Topics

# Actions

Division Problems pose a new challenge for us. We can't use the random number generator to create the number in the first position because we could get some very tricky problems. 

For example if you had to solve `61 / 7` you might not be able to figure out its `8.71413` without a calculator. Because of this we want to use numbers we know fall on the multiplication tables used in the previous step. 

To accomplish this we will generate two numbers just as we do with multiplication however to get our number in the first position we will use the result of mulitplying our `num_1` and `num_2` results.

```python
  num_1 = random.randint(2, 10)
  num_2 = random.randint(2, 10)
  multiplication_result = num_1 * num_2
  print(f"{multiplication_result} * {min(num_1, num_2)} = ______")
```
# Resources

[Multiplication Tables](https://en.wikipedia.org/wiki/Multiplication_table)