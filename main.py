from characters import Barbarian, Dragon, Elf, Knight, Wizard
import random as r
from clear import clear
import time
import pickle
import os

class Team:
    def __init__(self):
        
        self.creatures = [Barbarian, Dragon, Elf, Knight, Wizard]
        self.team = []

    def returnButton(self): # return button
        print('press [ENTER] to return')
        input()

    def random_creature(self): # creates a random creature class
        return r.choice(self.creatures)()

    def creature_viewer(self): # creature viewer menu
        clear()
        print('---------Team Viewer---------')
        self.print_creatues()  
        self.returnButton()

    def print_creatues(self): # prints creatures and their stats out
        for creature in self.team:
            time.sleep(0.1)
            details = creature.get_details()
            print('')
            print(f"Name: {details['name']}")
            print(f"    -Type: {details['type']}")
            print(f"    -Stats:")
            print(f"        -Health: {details['health']}")
            print(f"        -Power: {details['power']}")
            print(f"        -Special Attack Power: {details['special power']}")
            print(f"        -Speed: {details['speed']}")      

    def create_creatures(self, number): # adds creatures to the team 
        clear()
        print('---------Creature Creation---------')
        print('')
        print('creating:')
        time.sleep(0.5)
        for i in range(number):
                        addition = self.random_creature()
                        print(f'    -{addition.name} ({addition.type})')
                        self.team.append(addition)
                        time.sleep(0.5)
        
    def creature_creation(self): # creature creation menu
        running = True
        while running:
            clear()
            print('---------Creature Creation---------')
            print('')
            print(f'team size: {len(self.team)}')
            print('')
            print('Enter the number of creatures to be created:')

            try:
                selection = int(input(''))
                if 0 <= selection:
                    self.create_creatures(selection)
                    running = False
            except ValueError:
                print('Incorrect value entered, try again')
        self.returnButton()

    def purge_creature(self, index): # remoces a creature from the team
        deadCreature = self.team.pop(index)
        print(f'{deadCreature.name} has been terminated')
    
    def perge_screen(self):
        running = True
        while running:
            clear()
            print('-------Select which creature to perge-------')
            print('[press 0 to return]')
            for i, creature in enumerate(self.team):
                details = creature.get_details()
                print(f'{i+1}) {details["name"]} ({details["type"]})')
            
            try:
                selection = int(input(''))
                if 0 <= selection <= i+1:
                    if selection == 0:
                        running = False
                    else:
                        clear()
                        self.purge_creature(selection-1)
                        self.returnButton()

            except ValueError:
                print('Incorrect value entered, try again')

    def save_team(self): # saving the current team to a file
        clear()
        print('------Save Team------\n')
        name = input('enter team name: ')
        svTeam = SavedTeam(self.team, name)
        with open(f'./saves/{svTeam.savename}', 'wb') as file:
            pickle.dump(svTeam, file)
        print(f'team: {svTeam.savename} saved')
        self.returnButton()
    
    def load_team(self): #loading team from file
        saves = os.listdir('./saves')
        running = True
        while running:
            clear()
            for i, save in enumerate(saves):
                print(f'{i+1}) {save}')
            i += 1
            try:
                selected = int(input(f'select a saved team (1-{i}):\n'))
                if 0 < selected <= i:
                    with open(f'./saves/{saves[i-1]}', 'rb') as file:
                        newteam = pickle.load(file)
                    self.team = newteam.extract_team()
                    running = False
                    clear()
                    print(f'-------Team {saves[i-1]} loaded-------')
                    print('it contains:')
                    self.print_creatues()
            except ValueError:
                pass
        self.returnButton()

    
        

    def mainLoop(self): # mainloop / home menu
        running = True
        while running:
            clear()
            print('--------Menu-------')
            print(f'team size: {len(self.team)}')
            print('')
            print('1) View Team')
            print('2) add creatures to team')
            print('3) purge creature from team')
            print('4) save team')
            print('5) load team')
            try:
                selection = int(input(''))
                if 0 < selection <= 5:
                    if selection == 1:
                        self.creature_viewer()
                    elif selection == 2:
                        self.creature_creation()
                    elif selection == 3:
                        self.perge_screen()
                    elif selection == 4:
                        self.save_team()
                    elif selection == 5:
                        self.load_team()
                        

            except ValueError:
                print('Incorrect value entered, try again')
    

class SavedTeam:
    def __init__(self, team, name,):
        self._team = team
        self.savename = name
        
    
    def extract_team(self):
        return self._team
        
if __name__ == '__main__':
    main = Team()
    main.mainLoop()
