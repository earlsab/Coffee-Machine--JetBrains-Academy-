# machine state directly influences what info will be displayed
class CoffeeMachine:
    # list format [Water, Milk, CBeans, Cups needed, Money]
    #             [0]    [1]   [2]      [3]          [4]
    resource = [400, 540, 120, 9, 550]
    # espresso = [250, 0, 16, 1, 4]
    # latte = [350, 75, 20, 1, 7]
    # cappuccino = [200, 100, 12, 1, 6]
    exit = False
    machine_state = "main"
    resource_lacking = None
    fill_count = 0
    repeat = False

    def text(self):
        if self.machine_state == "main":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.machine_state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.machine_state == "buy success":
            self.machine_state = "buy"
            print("I have enough resources, making you coffee!")
            self.repeat = True
            self.machine_state = "main"
        elif self.machine_state == "buy fail":
            print(f"Sorry, not enough {(', '.join(self.resource_lacking))}!")
            self.repeat = True
            self.machine_state = "main"
        elif self.machine_state == "fill":
            if self.fill_count == 0:
                print("Write how many ml of water do you want to add:")
            elif self.fill_count == 1:
                print("Write how many ml of milk do you want to add:")
            elif self.fill_count == 2:
                print("Write how many grams of coffee beans do you want to add:")
            elif self.fill_count == 3:
                print("Write how many disposable cups of coffee do you want to add:")
            else:
                print("Error")
        elif self.machine_state == "take":
            print(f"I gave you ${self.resource[4]}")
            self.take()
            self.machine_state = "main"
            self.repeat = True
        elif self.machine_state == "remaining":
            self.remaining()
            self.machine_state = "main"
            self.repeat = True
        elif self.machine_state == "exit":
            self.exit = True

    def user_input(self, ui):
        if self.machine_state == "main":
            main_options = ["buy", "fill", "take", "remaining", "exit"]
            if ui in main_options:
                self.machine_state = ui
        elif self.machine_state == "buy":
            buy_options = ["1", "2", "3", "back"]
            if ui in buy_options:
                self.buy(ui)
        elif self.machine_state == "fill":
            try:
                ui = int(ui)
                if type(ui) == int:
                    self.fill(ui)
            except ValueError:
                pass

        elif self.machine_state == "take":
            pass

    def buy(self, choice):

        if choice == "back":
            self.machine_state = "main"
        else:
            self.resource_lacking = []
            if choice == "1":  # espresso
                self.resource_needed = [250, 0, 16, 1, 4]
            elif choice == "2":  # latte
                self.resource_needed = [350, 75, 20, 1, 7]
            elif choice == "3":  # cappuccino
                self.resource_needed = [200, 100, 12, 1, 6]

            if not self.resource[0] >= self.resource_needed[0]:
                self.resource_lacking.append("water")
            if not self.resource[1] >= self.resource_needed[1]:
                self.resource_lacking.append("milk")
            if not self.resource[2] >= self.resource_needed[2]:
                self.resource_lacking.append("coffee beans")
            if not self.resource[3] >= self.resource_needed[3]:
                self.resource_lacking.append("cups")

            if not self.resource_lacking:
                self.machine_state = "buy success"
                self.resource[0] -= self.resource_needed[0]
                self.resource[1] -= self.resource_needed[1]
                self.resource[2] -= self.resource_needed[2]
                self.resource[3] -= self.resource_needed[3]
                self.resource[4] += self.resource_needed[4]
            else:
                self.machine_state = "buy fail"

    def fill(self, amount):

        if self.fill_count == 0:
            self.resource[0] += amount
            self.fill_count = 1
        elif self.fill_count == 1:
            self.resource[1] += amount
            self.fill_count = 2
        elif self.fill_count == 2:
            self.resource[2] += amount
            self.fill_count = 3
        elif self.fill_count == 3:
            self.resource[3] += amount
            self.fill_count = 0
            self.machine_state = "main"

    def take(self):
        self.resource[4] -= self.resource[4]

    def remaining(self):
        print(f"""The coffee machine has:
{self.resource[0]} of water
{self.resource[1]} of milk
{self.resource[2]} of coffee beans
{self.resource[3]} of disposable cups
${self.resource[4]} of money""")


cm = CoffeeMachine()
while True:
    cm.text()

    if cm.repeat:
        cm.repeat = False
    elif not cm.exit:
        cm.user_input(input())
    else:
        break
