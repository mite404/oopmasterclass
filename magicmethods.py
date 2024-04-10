class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    # def __str__(self):
    #     return f"Archer with {self.hp} hp and {self.mana} mana and {self.arrows} arrows"

    def __repr__(self):
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    def __add__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        new_hp = self.hp + other.hp
        new_mana = self.mana + other.mana
        new_arrows = self.arrows + other.arrows
        return Archer(new_hp, new_mana, new_arrows)

    def __eq__(self, other):
        if not isinstance(other, Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp


archer1 = Archer(100, 100, 6)
archer2 = Archer(100, 100, 5)
print(archer1 < archer2)
