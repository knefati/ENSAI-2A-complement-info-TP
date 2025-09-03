import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    """
    A Pokemon of type Defender
    """

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the Defender type.

        Returns:
            float: the multiplier
        """
        return 1 + (self.attack_current + self.defense_current) / 200