class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n > ")
        global water
        global milk
        global beans
        global cups
        global money
        levels  = [[250, 0, 16, 1], [350, 75, 20, 1], [200, 100, 12, 1]]
        inventory = [self.water, self.milk, self.beans, self.cups]
        full_name = ["water", "milk", "coffee beans", "disposable cups"]
        short, x = [], 0
        if coffee_type == "back":
            pass
        elif coffee_type in ["1", "2", "3"]:
            for i in levels[int(coffee_type)-1]:
                if inventory[x] < i:
                    short.append(full_name[x])
                x += 1
            if len(short) > 0:
                for i in range(len(short)):
                    print("Sorry, not enough " + full_name[i] + "!")
            else:  
                if coffee_type == "1":
                    self.water -= 250
                    self.milk -= 0
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
                elif coffee_type == "2":
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
                elif coffee_type == "3":
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6
                print("I have enough resources, making you a coffee!\n")
     
    def fill(self):
        new_water = int(input("Write how many ml of water do you want to add:\n > "))
        global water
        self.water += new_water
        new_milk = int(input("Write how many ml of milk do you want to add:\n > "))
        global milk
        self.milk += new_milk
        new_beans = int(input("Write how many grams of coffee beans do you want to add:\n > "))
        global beans
        self.beans += new_beans
        new_cups = int(input("Write how many disposable cups of coffee do you want to add:\n > "))
        global cups
        self.cups += new_cups

    def take(self):
        global money
        print("I gave you $" + str(self.money))
        self.money = 0

    def main(self):
        while True:
            print("")
            selection = input("Write action (buy, fill, take, remaining, exit):\n > ")
            print("")
            if selection == "buy":
                self.buy()
            elif selection == "fill":
                self.fill()
            elif selection == "take":
                self.take()
            elif selection == "remaining":
                self.remaining()
            elif selection == "exit":
                break

CM1 = CoffeeMachine(400, 540, 90, 9, 550)
CM1.main()
