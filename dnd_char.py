from conversion_tables import *
import utils as ut


class DnDCharacter():
    def __init__(self, name="None", _class="None", _str=0, dex=0, con=0, _int=0, wis=0,
                 cha=0, skill_profs=[], prof_bonus=2, speed=30, level=1,
                 hit_die=6, hit_die_count=1, health=1):

        self.ac = 0
        self.languages = set()
        self.skill_prof = [0 for _ in range(18)]
        self.name = name
        self.stats = [_str, dex, con, _int, wis, cha]
        self.stat_bonus = [(i-10) // 2 for i in self.stats]
        self.initiative = self.stat_bonus[stat_index['dex']]
        self.pasive_perception = self.stat_bonus[stat_index['wis']] + prof_bonus + 10;
        self.saving_throws = [0 for _ in range(6)]
        self.save_prof = [0 for _ in range(6)]
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
        self.current_health = self.health
        self.background = "None"
        self.player_name = "None"
        self.race = "None"
        self.xp = 0
        self.spell_cast_mod = "int"
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
        self.equipment = []
        self.weapons = []
        self.abilities = dict()
        self.inspiration = 0
        self.temp_hp = 0
        self.death_fails = 0
        self.death_saves = 0

    def print_character(self):
        # Print Name, and player name
        lines = []
        padded_name = ut.padright(self.name, 75)
        lines.append(f'Name:{padded_name}')
        padded_race = ut.padright(self.race, 75)
        lines.append(f'Race:{padded_race}')
        padded_class = ut.padright(self._class, 74)
        lines.append(f'Class:{padded_class}')
        padded_alignment = ut.padright(self.alignment, 70)
        lines.append(f'Alignment:{padded_alignment}')
        padded_background = ut.padright(self.background, 69)
        lines.append(f'Background:{padded_background}')
        padded_level_xp = ut.padright(f'{self.level}, {self.xp} xp', 69)
        lines.append(f'Level & XP:{padded_level_xp}')
        lines.append("+-------------------------------------+  +-AC-------+ +-Ini------+ +-Speed-----+")
        p_insp = ut.padleft(self.inspiration, 3)
        p_ac = ut.padleft(self.ac, 10)
        if self.initiative < 0:
            p_init = ut.padleft(f'{self.initiative}', 10)
        else:
            p_init = ut.padleft(f'+{self.initiative}', 10)

        p_spd = ut.padleft(f'{self.speed}', 11)
        lines.append(f'| Inspiration                    [{p_insp}] |  |{p_ac}| |{p_init}| |{p_spd}|')

        lines.append(f'| Proficiency Bonus              [ +{self.prof_bonus}] |  +----------+ +----------+ +-----------+')

        lines.append(f'| Passive Wisdom (Perception)    [ {self.pasive_perception}] |  +-Hit Points--------------------------+')
        
        p_hp_max = ut.padright(f'{self.health}', 28)
        lines.append(f'+-------------------------------------+  | Maximum:{p_hp_max}|')

        str_idx = stat_index["str"]
        cha_idx = stat_index["cha"]
        dex_idx = stat_index["dex"]
        con_idx = stat_index["con"]
        int_idx = stat_index["int"]
        wis_idx = stat_index["wis"]

        raw_str = ut.padleft(f'{self.stats[str_idx]}', 3)
        raw_con = ut.padleft(f'{self.stats[con_idx]}', 3)
        raw_int = ut.padleft(f'{self.stats[int_idx]}', 3)
        raw_wis = ut.padleft(f'{self.stats[wis_idx]}', 3)
        raw_cha = ut.padleft(f'{self.stats[cha_idx]}', 3)
        raw_dex = ut.padleft(f'{self.stats[dex_idx]}', 3)

        str_bonus = self.stat_bonus[str_idx]
        cha_bonus = self.stat_bonus[cha_idx]
        wis_bonus = self.stat_bonus[wis_idx]
        dex_bonus = self.stat_bonus[dex_idx]
        con_bonus = self.stat_bonus[con_idx]
        int_bonus = self.stat_bonus[int_idx]

        p_str = ut.build_bonus(str_bonus)
        p_cha = ut.build_bonus(cha_bonus)
        p_int = ut.build_bonus(int_bonus)
        p_con = ut.build_bonus(con_bonus)
        p_dex = ut.build_bonus(dex_bonus)
        p_wis = ut.build_bonus(wis_bonus)

        p_str_sv = ut.build_bonus(self.saving_throws[str_idx])
        p_cha_sv = ut.build_bonus(self.saving_throws[cha_idx])
        p_int_sv = ut.build_bonus(self.saving_throws[int_idx])
        p_con_sv = ut.build_bonus(self.saving_throws[con_idx])
        p_wis_sv = ut.build_bonus(self.saving_throws[wis_idx])
        p_dex_sv = ut.build_bonus(self.saving_throws[dex_idx])

        p_death_saves = ut.build_saves(self.death_saves)
        p_death_fails = ut.build_saves(self.death_fails)

        skills = []
        for skill in self.skill_bonus:
            skills.append(ut.build_bonus(skill))

        p_tmp_hp = ut.padright(f'{self.temp_hp}', 28)
        lines.append(f'| STRENGTH                  [{raw_str}] [{p_str}] |  | Temp HP:{p_tmp_hp}|')

        p_cur_hp = ut.padright(f'{self.current_health}', 28)
        lines.append(f'| Saving Throws                  [{p_str_sv}] |  | Current:{p_cur_hp}|')

        p_ath = skills[skill_index['ath']]
        p_hitdice = ut.padright(f'{self.hit_die_curent}d{self.hit_die}', 27)
        lines.append(f'| Athlethics                    [{p_ath}] |  | Hit Dice:{p_hitdice}|')

        lines.append('+-------------------------------------+  +-Death Saves-------------------------+')

        #do level 16
        lines.append(f'| DEXTERITY               [{raw_dex}] [{p_dex}] |  | Successes               {p_death_saves} |')

        lines.append(f'| Saving Throws                 [{p_dex_sv}] |  | Failures                {p_death_fails} |')

        p_acro = skills[skill_index['acro']]
        lines.append(f'| Acrobatics                    [{p_acro}] |  +-------------------------------------+')

        p_soh = skills[skill_index['soh']]
        lines.append(f'| Sleight of Hand               [{p_soh}] |  | WISDOM                  [{raw_wis}] [{wis_bonus}] |')

        p_stl = skills[skill_index['stl']]
        lines.append(f'| Stealth                       [{p_stl}] |  | Saving Throws                 [{p_wis_sv}] |')

        p_anhan = skills[skill_index['anhan']]
        lines.append(f'+-------------------------------------+  | Animal Handling               [{p_anhan}] |')

        p_ins = skills[skill_index['ins']]
        lines.append(f'| CONSTITUTION            [{raw_con}] [{p_con}] |  | Insight                       [{p_ins}] |')

        p_med = skills[skill_index['med']]
        lines.append(f'| Saving Throws                 [{p_con_sv}] |  | Medicine                      [{p_med}] |')

        p_perc = skills[skill_index['perc']]
        lines.append(f'+-------------------------------------+  | Perception                    [{p_perc}] |')

        p_sur = skills[skill_index['sur']]
        lines.append(f'| INTELLIGENCE            [{raw_int}] [{p_int}] |  | Survival                      [{p_sur}] |')

        lines.append(f'| Saving Throws                 [{p_int_sv}] |  +-------------------------------------+')

        p_arc = skills[skill_index['arc']]
        lines.append(f'| Arcana                        [{p_arc}] |  | CHARISMA                [{raw_cha}] [{p_cha}] |')
        
        p_his = skills[skill_index['his']]
        lines.append(f'| History                       [{p_his}] |  | Saving Throws                 [{p_cha_sv}] |')

        p_inv = skills[skill_index['inv']]
        p_dec = skills[skill_index['dec']]
        lines.append(f'| Investigation                 [{p_inv}] |  | Deception                     [{p_dec}] |')
        
        p_nat = skills[skill_index['nat']]
        p_intim = skills[skill_index['intim']]
        lines.append(f'| Nature                        [{p_nat}] |  | Intimidation                  [{p_intim}] |')

        p_rel = skills[skill_index['rel']]
        p_perf = skills[skill_index['perf']]
        lines.append(f'| Religion                      [{p_rel}] |  | Performance                   [{p_perf}] |')

        p_pers = skills[skill_index['pers']]
        lines.append(f'+-------------------------------------+  | Persuation                    [{p_pers}] |')

        lines.append('+-Other Proficiencies and Languages---+--+-------------------------------------+')

        for lang in self.languages:
            line = ut.padright(f'|{lang}', 79) + '|'
            lines.append(line)

        for prof in self.misc_profs:
            line = ut.padright(f'|{prof}', 79) + '|'
            lines.append(line)

        lines.append("+-Weapon--------+-ATK D.-+-Damage/Typ-+-Properties--------------------+--Stat--+")

        for weap in self.weapons:
            p_w = ut.padleft(weap.name, 15)
            p_d = ut.padleft(f'{weap.damage_die_count}d{weap.damage_die}', 8)
            p_t = ut.padleft(weap.damage_type, 12)
            p_s = ut.padleft(weap.base_stat, 8)
            p_p = ut.padleft(weap.properties, 31)
            lines.append(f'|{p_w}|{p_d}|{p_t}|{p_p}|{p_s}|')

        lines.append('+-------------+ +--------+----+ +--------------+ +-------------+ +----+--------+')

        p_pp = ut.padleft(f'{self.platinum}', 6)
        p_gp = ut.padleft(f'{self.gold}', 6)
        p_ep = ut.padleft(f'{self.electrum}', 7)
        p_sp = ut.padleft(f'{self.silver}', 6)
        p_cp = ut.padleft(f'{self.copper}', 6)
        lines.append(f'| PP [{p_pp}] | | GP [{p_gp}] | | EP [{p_ep}] | | SP [{p_sp}] | | CP [{p_cp}] |')

        lines.append('+-------------+ +-------------+ +--------------+ +-------------+ +-------------+')

        lines.append('+-Equipment---+-+-------------+-+--------------+-+-------------+-+-------------+')

        for eq in self.equipment:
            line = ut.padright(f'|{eq}', 79) + '|'
            lines.append(line)

        lines.append('+-Features---------------------------------------------------------------------+')

        for (name, description) in self.abilities.items():
            line = ut.padright(f'|{name}:', 79) + '|'
            lines.append(line)
            des_lines = ut.segment(description, 78)
            for dl in des_lines:
                line = ut.padright(f'|{dl}', 79) + '|'
                lines.append(line)

        for pt in self.personality:
            line = ut.padright(f'|{pt}', 79) + '|'
            lines.append(line)

        for ideal in self.ideals:
            line = ut.padright(f'|{ideal}', 79) + '|'
            lines.append(line)

        for bond in self.bonds:
            line = ut.padright(f'|{bond}', 79) + '|'
            lines.append(line)

        for flaw in self.flaws:
            line = ut.padright(f'|{flaw}', 79) + '|'
            lines.append(line)

        for line in lines:
            print(line)
        pass

    def set_stat(self, stat_name, stat_value):
        index = stat_index[stat_name]
        self.stats[index] = stat_value
        self.stat_bonus[index] = (stat_value - 10) // 2
        if stat_name == 'wis':
            self.pasive_perception = self.stat_bonus[stat_index['wis']] + self.prof_bonus + 10;

        self.update_skills(stat_name)

    def update_skills(self, base_stat):
        i = stat_index[stat]
        self.saving_throws[i] = self.save_prof[i] * self.prof_bonus + self.skill_bonus[i]
        prof = self.prof_bonus * self.skill_prof[i]
        self.skill_bonus[i] = prof + self.stat_bonus[i]

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

        for (key, value) in abilities.items():
            new_char.abilities[key] = value

        print("Input any racial skill proficiencies you have then input 'q' to quit\n")
        proficiencies = set()
        proficiency = input("Enter a proficiency: ")
        print("To remove a mistake enter 'x [proficiency]'")
        while (proficiency != 'q'):
            if proficiency[0] == 'x':
                proficiencies.remove(' '.join(proficiency.split(' ')[1:]))
            else:
                proficiencies.add(proficiency)
            proficiency = input("Enter a proficiency: ")

        for p in proficiencies:
            new_char.skill_prof.add(p)

        print("Input any other racial proficiencies you have then input 'q' to quit\n")
        proficiencies = set()
        proficiency = input("Enter a proficiency: ")
        print("To remove a mistake enter 'x [proficiency]'")
        while (proficiency != 'q'):
            if proficiency[0] == 'x':
                proficiencies.remove(' '.join(proficiency.split(' ')[1:]))
            else:
                proficiencies.add(proficiency)
            proficiency = input("Enter a proficiency: ")

        for p in proficiencies:
            new_char.misc_profs.add(p)

        print("Input any ability score improvements, then the bonus amount. When you are finished input an ability name 'q'\n")
        print("To remove a mistake enter 'x [stat name]'")
        ability_scores = dict()
        stat_name = input("Enter a stat name: ")
        while stat_name != 'q':
            if stat_name[0] == 'x':
                ability_scores.remove(' '.join(stat_name.split(' ')[1:]))
            else:
                ability_score = int(input(f'Bonus to {stat_name}: '))
                ability_scores[ability_name] = ability_score

            ability_name = input("Enter a stat name: ")

        for (key, value) in ability_scores.items():
            stat_idx = stat_index[key]
            old_stat = new_char.stats[stat_idx]
            new_char.set_stat(key, old_stat + value)

    def chose_class(new_char):
        pass

    def create_character():
        new_char = DnDCharacter()
        player_name = input("What is your (real life) name? ")
        new_char.player_name = player_name

        # Sets race, some proficiencies, some ability score modifiers, and
        # some languages
        chose_race(new_char)

        chose_class(new_char)

        return new_char


me = create_character()

