import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    """
    A Pokemon of type All rounder
    """

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the All rounder type.

        Returns:
            float: the multiplier
        """
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200