from math import ceil

class Weapon:
    def __init__(self, type="", name="", atk=0, crit_chance=None, element=[], exp=0, level=1):
        self.type = type
        self.name = name
        self.atk = atk
        self.crit_chance = crit_chance
        self.element = element
        self.exp = exp
        self.level = level

    def increment_exp(self, exp):
        self.exp += exp
        if self.exp > 99:
            levels = self.exp // 100
            self.level_up(levels)

    def element_check(self, element):
        if element in self.element:
            self.add_element(existent=True)
        else:
            self.element.append(element)
            return True

    def add_element(self, existent=False):
        if existent:
            print("Your weapon already has that element.")

        element = input("Choose a new element for your weapon\nA. Fire\nB. Ice\nC. Wind\nD. Water\n")

        if element == "a":
            added = self.element_check("Fire")

        elif element == "b":
            added = self.element_check("Ice")

        elif element == "c":
            added = self.element_check("Wind")

        elif element == "d":
            added = self.element_check("Water")

        if added:
            print(f"Your weapon now has the power of {self.element[len(self.element)-1]}!")

    def level_up(self, levels):
        if levels > 1:
            for i in range(levels):
                self.level += 1
                atk_increase = (self.atk * 10 / 100)
                self.exp -= 100
                self.atk += ceil(atk_increase)
                print(f"{self.name} leveled up! Its level is now {self.level}.\n Its ATK is now {self.atk}")

        else:
            self.level += 1
            atk_increase = (self.atk * 10 / 100)
            self.exp -= 100
            self.atk += ceil(atk_increase)
            print(f"{self.name} leveled up! Its level is now {self.level}.\n Its ATK is now {self.atk}")

        if self.level == 10:
            self.exp = 0
            selection = input("Weapon level max!! How would you like to augment your weapon?\nA. ATK\nB. Crit Chance\nC. Element\n").lower()

            if selection == "a":
                self.atk += 50
                print(f"Weapon ATK increased by 50! ATK is now {self.atk}.")

            elif selection == "b":
                self.crit_chance += 15
                print(f"Weapon Critical Hit Chance increased by 15! Critical Hit Chance is now {self.crit_chance}.")

            elif selection == "c":
                self.add_element()

    def list_elements(self):
        print("Your weapon has the following elements:")
        for el in self.element:
            print(el)

class Armor:
    def __init__(self, type="", name="", defence=0, crit_resist=None, elemental_resist=None):
        self.type = type
        self.name = name
        self.defence = defence
        self.crit_resist = crit_resist
        self.elemental_resist = elemental_resist

firebrand = Weapon(type="Broadsword", name="Firebrand", atk=100, crit_chance=8, element=["Fire"])
diamond_dagger = Weapon(type="knife", name="Diamond Dagger", atk=175, crit_chance=20)

firebrand.increment_exp(900)
firebrand.list_elements()

# diamond_dagger.level_up(3)