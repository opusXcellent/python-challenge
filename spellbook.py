#spellbook.py

spellbook = {
    "Fireball": "Creates a ball of fire.",
    "Heal": "Restores health.",
    "Invisibility": "Makes you invisible."
}
print(spellbook)

spellbook["Teleport"] = "Transports you to another location instantly."
print(spellbook)

spellbook.pop("Invisibility")
print(spellbook)

for key, value in spellbook.items():
    print(f"Spell: {key} -> Effect: {value}")