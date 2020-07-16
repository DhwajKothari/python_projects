# Write your code here
class CoffeeMachine:
    def __init__(self, water = 0, milk = 0, beans = 0, cups = 0, money = 0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def display(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def buy(self):
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if order == "1":
            if self.water < 250:
                print("Not enough water")
            elif self.beans < 16:
                print("Not enough coffee beans")
            elif self.cups < 1:
                print("Not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif order == "2":
            if self.water < 350:
                print("Not enough water")
            elif self.milk < 75:
                print("Not enough milk")
            elif self.beans < 20:
                print("Not enough coffee beans")
            elif self.cups < 1:
                print("Not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif order == "3":
            if self.water < 350:
                print("Not enough water")
            elif self.milk < 75:
                print("Not enough milk")
            elif self.beans < 20:
                print("Not enough coffee beans")
            elif self.cups < 1:
                print("Not enough disposable cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
        else:
            pass
        
    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def fill(self):
        addedWater = int(input("Write how many ml of water do you want to add:"))
        self.water += addedWater
        addedMilk = int(input("Write how many ml of milk do you want to add:"))
        self.milk += addedMilk
        addedBeans = int(input("Write how many grams of coffee beans do you want to add:"))
        self.beans += addedBeans
        addedCups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups += addedCups

    def func(self,action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        else:
            self.display()


    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "exit":
                break
            self.func(action)

my_coffee_machine = CoffeeMachine(500, 450, 100, 9, 550)
my_coffee_machine.start()
