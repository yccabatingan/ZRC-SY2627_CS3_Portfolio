class Hero:
    def __init__(self, name, hp):
        # TODO: store `name` and `hp` as INSTANCE attributes
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        # TODO: subtract `amount` from this hero's hp
        self.hp = self.hp - amount
        return self.hp

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

print(arthur.hp)
print(arthur.take_damage(10))
