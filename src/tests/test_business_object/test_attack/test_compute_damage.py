from src.business_object.pokemon.abstractPokemon import AttackerPokemon, FixedDamageAttack
from src.business_object.statistic import Statistic

class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        attacker = AttackerPokemon(stat_current=Statistic(attack=100, defense=100))
        defender = AttackerPokemon(stat_current=Statistic(attack=100, defense=100))
        attack = FixedDamageAttack(power=50, name="Tackle", description="A basic physical attack")

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 50

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
