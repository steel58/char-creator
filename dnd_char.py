from conversion_tables import *


class DnDCharacter():
    def __init__(self, name="", _class="", _str=0, dex=0, con=0, _int=0, wis=0,
                 cha=0, skill_profs=[], prof_bonus=2, speed=30, level=1,
                 hit_die=6, hit_die_count=1, health=1):

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

    def chose_race():
        input("What race would you like your character to be? ")
        pass

    def create_character():
        chose_race()
