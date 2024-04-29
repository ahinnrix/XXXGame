#=====================================================================================
#Amanda Hinnerichs
#April 28, 2024
#Assignment XXXGame.py
#Description: Game where character can loose or gain stamina based on actions.

#====================================================================================
class GameCharacter:
    def __init__(self, name, stamina, action):
        self.name = name
        self.stamina = stamina
        self.action = action

        def walk(self):
            print(f"{self.name} is marching with the band.")
            self.stamina = max (self.stamina -5, 0)
            self.action = 'march'
            print(f"{self.name}'s stamina decreased to {self.stamina}.")

        def rest(self):
            print(f'{self.name} is resting.')
            self.stamina += 20
            self.action = 'rest'
            print(f"{self.name}'s stamina increased to {self.stamina}.")

        def solo(self):
            print(f"{self.name} .")
            self.stamina -= 10
            self.action = 'solo'
            print(f"{self.name}'s stamina decreased to {self.stamina}.")

        def audition(self):
            print(f'{self.name} audition for the Band .')
            self.stamina -= 10
            self.action = 'Audition'
            print(f"{self.name}'s stamina decreased to {self.stamina}.")

    def help(self):
        print("        Stamina")
        print("m = march     -5\nr = rest        +20\ns = solo      -10-\na = audition        -20\nq = quit")
        print(f"{self.name}'s last action was {self.action}.")

class instrument():
    def __init__(self, name: str, instrument_type: str, stamina: int):
        self.name = name
        self.instrument_type = instrument_type
        self.stamina = 0
        self.action = input(f"{self.name} is playing the {self.instrument}")


class music_man(GameCharacter):
    def __init__(self, name, stamina):
        super().__init__(name=name, stamina=stamina)
        self.instrument_type = 'music_man'

class tiny_dancer(GameCharacter):
    def __init__(self, name, stamina):
        super().__init__(name=name, stamina=stamina)
        self.instrument_type = 'tiny_dancer'

#=====================================================================================
#music_man = (name ="Music_Man", stamina =50, action = 'march')
#tiny_dancer = (name = "Tiny_Dancer", stamina =50, action = 'solo')
#flute = instrument_type(name = "Flute")
#drums = instrument(name = "Drums")
#trumpet = instrument(name = "Trumpet")
#bass = instrument(name = bass)
#mandolin = instrument(name = "Mandolin")