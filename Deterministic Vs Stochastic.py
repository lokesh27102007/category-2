import random

print("Deterministic Environment")

a = 5
b = 3

print("Addition:", a + b)

print("Stochastic Environment")

result = random.choice(["Success", "Failure"])

print("Result:", result)
