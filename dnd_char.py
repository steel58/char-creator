from conversion_tables import *


class DnDCharacter():
    def __init__(self, name="", _class="", _str=0, dex=0, con=0, _int=0, wis=0,
                 cha=0, skill_profs=[], prof_bonus=2, speed=30, level=1,
                 hit_die=6, hit_die_count=1, health=1):

        self.languages = set()
        self.skill_prof = [0 for _ in range(18)]
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.initiative = self.stat_bonus[stat_index['dex']]
        self.pasive_perception = self.stat_bonus[stat_index['wis']] + prof_bonus + 10;
        self.saving_throws = [0 for _ in range(6)]
        self.skill_bonus = [0 for _ in range(18)]
        self.misc_profs = []
        self.prof_bonus = prof_bonus
        self.class_ = _class
        self.speed = speed
        self.level = level
        self.hit_die = hit_die
        self.hit_die_max = hit_die_count
        self.hit_die_curent = hit_die_count
        self.health = self.hit_die + self.stat_bonus[2]
        self.background = ""
        self.player_name = ""
        self.race = ""
        self.xp = 0
        self.personality = []
        self.ideals = []
        self.bonds = []
        self.flaws = []
        self.copper = 0
        self.silver = 0
        self.gold = 0
        self.electrum = 0
        self.platinum = 0
        self.spell_slots = [0 for _ in range(9)]
        self.spells_cantrip = []
        self.spells_lvl1 = []
        self.spells_lvl2 = []
        self.spells_lvl3 = []
        self.spells_lvl4 = []
        self.spells_lvl5 = []
        self.spells_lvl6 = []
        self.spells_lvl7 = []
        self.spells_lvl8 = []
        self.spells_lvl9 = []

    def set_stat(self, stat_name, stat_value):
        index = stat_index[stat_name]
        self.stats[index] = stat_value
        self.stat_bonus[index] = (stat_value - 10) // 2
        if stat_name == 'wis':
            self.pasive_perception = self.stat_bonus[stat_index['wis']] + self.prof_bonus + 10;

        self.update_skills(stat_name)

    def update_skills(self, base_stat):
        for (i, stat) in enumerate(self.skill_base):
            if stat == base_stat:
                stat_index = stat_index[stat]
                prof = self.prof_bonus * self.skill_prof[i]
                self.skill_bonus[i] = prof + self.stat_bonus[stat_index]

    def get_bonus(self, word):
        if word in self.stat_index:
            return self.stat_bonus[stat_index[word]]
        elif word.lower() in self.skill_index:
            return self.skill_bonus[skill_index[word]]
        elif word.lower() == 'prof' or word.lower() == 'proficiency':
            return self.prof_bonus
        else:
            return "This is not a valid skill or stat"

    def from_dict(self, _dict):
        for trait in _dict:
            setattr(self, trait, _dict[trait])
        return self

    def currency_convert(count, start, finish):
        if start.lower()[0] == "c":
            return copper_convert[finish.lower()[0]] * count
        elif start.lower()[0] == "s":
            return silver_convert[finish.lower()[0]] * count
        elif start.lower()[0] == "e":
            return electrum_convert[finish.lower()[0]] * count
        elif start.lower()[0] == "g":
            return gold_convert[finish.lower()[0]] * count
        elif start.lower()[0] == "p":
            return platinum_convert[finish.lower()[0]] * count
        else:
            return None

    def chose_race(new_char):
        race = input("What race would you like your character to be? ")
        new_char.race = race
        size = input("What size is your race? ")
        new_char.size = size
        speed = int(input("What is the speed of your race? "))
        new_char.speed = speed

        print("Input any languages your race can speak then input 'q' to quit\n")
        print("To remove a mistake enter 'x [language]'")
        languages = set()
        language = input("Enter a language: ")
        while (language != 'q'):
            if language[0] == 'x':
                languages.remove(' '.join(language.split(' ')[1:]))
            else:
                languages.add(language)
            language = input("Enter a language: ")

        new_char.languages = languages

        print("Input any abilities, then their description. When you are finished input an ability name 'q'\n")
        print("To remove a mistake enter 'x [ability name]'")
        abilities = dict()
        ability_name = input("Enter an ability name: ")
        while ability_name != 'q':
            if ability_name[0] == 'x':
                abilities.remove(' '.join(ability_name.split(' ')[1:]))
            else:
                ability_description = input(f'Description of {ability_name}: ')
                abilities[ability_name] = ability_description
            ability_name = input("Enter an ability name: ")

        print("Input any racial proficiencies you have then input 'q' to quit\n")
        proficiencies = set()
        proficiency = input("Enter a proficiency: ")
        print("To remove a mistake enter 'x [proficiency]'")
        while (proficiency != 'q'):
            if proficiency[0] == 'x':
                proficiencies.remove(' '.join(proficiency.split(' ')[1:]))
            else:
                proficiencies.add(proficiency)
            proficiency = input("Enter a proficiency: ")

        print("Input any ability score improvements, then the bonus amount. When you are finished input an ability name 'q'\n")
        print("To remove a mistake enter 'x [stat name]'")
        ability_scores = dict()
        stat_name = input("Enter a stat name: ")
        while stat_name != 'q':
            if stat_name[0] == 'x':
                ability_scores.remove(' '.join(stat_name.split(' ')[1:]))
            else:
                ability_score = input(f'Bonus to {stat_name}: ')
                ability_scores[ability_name] = ability_score

            ability_name = input("Enter a stat name: ")

    def create_character():
        new_char = DnDCharacter()
        chose_race(new_char)
