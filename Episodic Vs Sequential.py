print("Episodic Environment")

images = ["Cat", "Dog", "Car"]

for image in images:
    print("Classifying:", image)

print("Sequential Environment")

position = 0

actions = [1, 1, -1]

for action in actions:
    position = position + action
    print("Position:", position)
