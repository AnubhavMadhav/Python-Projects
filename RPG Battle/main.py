from classes.game import Person, bcolors

magic = [{"name": "Thor", "cost": 10, "dmg":60},
         {"name": "Hulk", "cost": 10, "dmg":60},
         {"name": "Krrish", "cost": 10, "dmg":60}]

player = Person(400, 65, 60, 34, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_spell_damage(2))