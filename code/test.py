

import random
import time

# Print the welcome message
print("Welcome to the rocket launch game!")

# Ask the user for the number of rocket launches
num_launches = int(input("How many rocket launches would you like? "))

# Loop through the number of rocket launches
for launch in range(num_launches):
    print("Launching rocket #{}".format(launch + 1))
    time.sleep(random.randint(1, 10))
    print("Liftoff!")

# Print the goodbye message
print("Goodbye!")
