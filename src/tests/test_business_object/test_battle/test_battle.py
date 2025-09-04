import pytest

from src.business_object.battle import BattleService, Battle, Round
from src.business_object.pokemon.abstractPokemon import AttackerPokemon, DefenderPokemon, PhysicalAttack, SpecialAttack
from src.business_object.statistic import Statistic


class TestBattleService:
    def test_resolve_battle(self):
        # GIVEN
        attacker = AttackerPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        defender = DefenderPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)

        physical_attack = PhysicalAttack(power=50, name="Tackle", description="A basic physical attack")
        special_attack = SpecialAttack(power=50, name="Ember", description="A basic special attack")

        attacker.attacks = [physical_attack]
        defender.attacks = [special_attack]

        battle_service = BattleService()

        # WHEN
        battle = battle_service.resolve_battle(attacker, defender)

        # THEN
        assert isinstance(battle, Battle)
        assert battle.winner is not None
        assert isinstance(battle.rounds, list)
        assert all(isinstance(round, Round) for round in battle.rounds)

    def test_get_order(self):
        # GIVEN
        pokemon1 = AttackerPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        pokemon2 = DefenderPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)

        battle_service = BattleService()

        # WHEN
        attacker, defender = battle_service.get_order(pokemon1, pokemon2)

        # THEN
        assert attacker is pokemon1 or attacker is pokemon2
        assert defender is pokemon1 or defender is pokemon2
        assert attacker is not defender

    def test_choose_attack(self):
        # GIVEN
        pokemon = AttackerPokemon(stat_current=Statistic(attack=100, defense=100, sp_atk=100, sp_def=100, speed=100, hp=100), level=50)
        physical_attack = PhysicalAttack(power=50, name="Tackle", description="A basic physical attack")
        special_attack = SpecialAttack(power=50, name="Ember", description="A basic special attack")

        pokemon.attacks = [physical_attack, special_attack]

        battle_service = BattleService()

        # WHEN
        chosen_attack = battle_service.choose_attack(pokemon)

        # THEN
        assert chosen_attack in [physical_attack, special_attack]

if __name__ == "__main__":
    pytest.main([__file__])
