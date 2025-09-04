import random
from typing import List, Tuple

from src.business_object.pokemon.abstractPokemon import AbstractPokemon, AbstractAttack


class Battle:
    def __init__(self, first_monster: AbstractPokemon, second_monster: AbstractPokemon):
        self.first_monster = first_monster
        self.second_monster = second_monster
        self.winner = None
        self.rounds = []

class Round:
    def __init__(self, attacker: AbstractPokemon, defender: AbstractPokemon, dealt_damage: int, attack_description: str):
        self.attacker = attacker
        self.defender = defender
        self.dealt_damage = dealt_damage
        self.attack_description = attack_description

class BattleService:
    def resolve_battle(self, pokemon1: AbstractPokemon, pokemon2: AbstractPokemon) -> 'Battle':
        """
        Resolve a battle between two Pokémon.

        Args:
            pokemon1 (AbstractPokemon): The first Pokémon.
            pokemon2 (AbstractPokemon): The second Pokémon.

        Returns:
            Battle: The result of the battle.
        """
        battle = Battle(pokemon1, pokemon2)
        current_round = 1

        while not pokemon1.is_ko() and not pokemon2.is_ko():
            attacker, defender = self.get_order(pokemon1, pokemon2)
            attack = self.choose_attack(attacker)
            damage = attack.compute_damage(attacker, defender)
            defender.get_hit(damage)

            round_info = Round(attacker, defender, damage, attack.description)
            battle.rounds.append(round_info)
            current_round += 1

        battle.winner = pokemon1 if pokemon2.is_ko() else pokemon2
        return battle

    def get_order(self, pokemon1: AbstractPokemon, pokemon2: AbstractPokemon) -> Tuple[AbstractPokemon, AbstractPokemon]:
        """
        Determine the order of attack based on the speed of the Pokémon.

        Args:
            pokemon1 (AbstractPokemon): The first Pokémon.
            pokemon2 (AbstractPokemon): The second Pokémon.

        Returns:
            Tuple[AbstractPokemon, AbstractPokemon]: The attacker and defender in order.
        """
        if pokemon1.speed_current >= pokemon2.speed_current:
            return pokemon1, pokemon2
        else:
            return pokemon2, pokemon1

    def choose_attack(self, pokemon: AbstractPokemon) -> AbstractAttack:
        """
        Choose an attack for the Pokémon.

        Args:
            pokemon (AbstractPokemon): The Pokémon.

        Returns:
            AbstractAttack: The chosen attack.
        """
        # For simplicity, we'll assume the Pokémon has a list of attacks
        # and we choose one randomly. In a real implementation, this could
        # be more complex.
        return random.choice(pokemon.attacks)
