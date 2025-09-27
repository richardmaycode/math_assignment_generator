# 8 Implement Multiplication Problem Creation

# Topics Covered

- No New Topics

# Actions

When creating multiplication problems we have discovered a new requirement; the user only knows multiplication tables up to 10, so they won't be able to solve math problems like `80 * 32`. Additionally, they would be bored with anything mulitplied by `1` so they have asked to only use the times tables between 2 and 10. This means we have to adjust our randomint() output to be within the range `2, 10`

```python
  num_1 = random.randint(2, 10)
  num_2 = random.randint(2, 10)
  print(f"{max(num_1, num_2)} * {min(num_1, num_2)} = ______")
```
# Resources

[Multiplication Tables](https://en.wikipedia.org/wiki/Multiplication_table)
