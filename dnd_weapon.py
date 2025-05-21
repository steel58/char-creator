class DnDWeapon():
    def __init__(self, name, base_stat, damage_die,
                 damage_die_count=1, proficiency=True, damage_type="Pierce"):
        self.name = name
        self.base_stat = base_stat
        self.damage_die = damage_die
        self.damage_die_count = damage_die_count
        self.damage_type = damage_type
        self.proficiency = proficiency
        self.properites = ""
