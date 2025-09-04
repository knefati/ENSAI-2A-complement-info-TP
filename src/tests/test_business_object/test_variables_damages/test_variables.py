import pytest

from src.business_object.pokemon.abstractPokemon import AttackerPokemon, DefenderPokemon, PhysicalAttack, SpecialAttack
from src.business_object.statistic import Statistic


class TestVariableDamageAttacks:
    def test_physical_attack(self):
        # GIVEN
        attacker = AttackerPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        attack = PhysicalAttack(power=50, name="Tackle", description="A basic physical attack")

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert isinstance(damage, int)
        assert damage > 0

    def test_special_attack(self):
        # GIVEN
        attacker = AttackerPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        attack = SpecialAttack(power=50, name="Ember", description="A basic special attack")

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert isinstance(damage, int)
        assert damage > 0

if __name__ == "__main__":
    pytest.main([__file__])
