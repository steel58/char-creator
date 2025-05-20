from bs4 import BeautifulSoup
import requests as re


base_link = "https://dnd5e.wikidot.com/spell:"


class DNDSpell:
    def __init__(self, title, level, _type, duration, components, _range,
                 casting_time, description, link, damage=None):
        self.title = title
        self.level = level
        self._type = _type
        self.duration = duration
        self.components = components
        self._range = _range
        self.casting_time = casting_time
        self.description = description
        self.link = link
        self.damage = damage

    def print_spell(self):
        print(f'{self.title}:')
        if self.level == 0:
            print(f'{self._type} cantrip')
        else:
            print(f'Level-{self.level} {self._type}')
        print(f'    Casting Time: {self.casting_time}')
        print(f'    Range: {self._range}')
        print(f'    Components: {self.components}')
        print(f'    Duration: {self.duration}')
        if self.damage:
            print(f'    Damage: {self.damage}')

        print(f'\n{self.description}')
        print(f'\n{self.link}')


def lookup_spell(name):
    name = name.lower()
    name.replace(" ", "-")
    lookup_link = base_link + name

    page = re.get(lookup_link).text
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find(id="page-content")
    sections = content.find_all('p')
    # get level and type
    level_text = sections[1].contents[0].string.split(" ")
    if level_text[0][0].isdigit():
        level = int(level_text[0][0])
        _type = level_text[1]
    else:
        level = 0
        _type = level_text[0]

    # get casting time, range, components, and duration
    details = str(sections[2]).split("<br/>")
    cast_time = details[0].split('>')[-1].strip()
    _range = details[1].split('>')[-1].strip()
    components = details[2].split('>')[-1].strip()
    duration = details[3].split('>')[-2][0:-3].strip()

    # get huge text block
    text_sections = sections[3:-1]
    description = ""
    for p in text_sections:
        description += p.get_text()
        description += '\n\n'

    description = description.strip()
    return DNDSpell(name.lower(), level, _type, duration, components, _range,
                    cast_time, description, lookup_link)
