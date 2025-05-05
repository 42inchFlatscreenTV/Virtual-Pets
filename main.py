class Pet():
    def __init__(self, name, age=0, hunger=5, boredom=3, sleepiness=3):
        self.dead = False

####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)
        self.name = name
        self.age = age
        self.hunger = hunger
        self.boredom = boredom
        self.sleepiness = sleepiness
        self.dead = False
####----Task 2----####
#instantiate your pet object with the name of your choice
pet = Pet("Bobby")
####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness
def feed(self):
    self.hunger -= 3
    if self.hunger < 0:
        self.hunger = 0
    print(f"{self.name} has been fed. Hunger is now {self.hunger}.")

def play(self):
    self.boredom -= 3
    if self.boredom < 0:
        self.boredom = 0
    print(f"{self.name} has played. Boredom is now {self.boredom}.")

def sleep(self):
    self.sleepiness -= 5
    if self.sleepiness < 0:
        self.sleepiness = 0
    print(f"{self.name} has slept. Sleepiness is now {self.sleepiness}.")

def wait(self):
    self.age += 1
    self.hunger += 1
    self.boredom += 1
    self.sleepiness += 1
    print(f"{self.name} has waited. Age is now {self.age}, Hunger is now {self.hunger}, Boredom is now {self.boredom}, Sleepiness is now {self.sleepiness}.")

def is_dead(self):
    if self.hunger >= 10 or self.boredom >= 10 or self.sleepiness >= 10 or self.age >= 15:
        self.dead = True
        print(f"{self.name} is dead.")
    else:
        print(f"{self.name} is alive.")
###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)