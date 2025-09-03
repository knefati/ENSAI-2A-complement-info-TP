import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    """
    A Pokemon of type Attacker
    """

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the Attacker type.

        Returns:
            float: the multiplier
        """
        return 1 + (self.speed_current + self.attack_current) / 200