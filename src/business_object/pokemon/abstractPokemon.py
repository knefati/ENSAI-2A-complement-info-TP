import copy
from abc import ABC, abstractmethod

from src.business_object.statistic import Statistic


class AbstractPokemon(ABC):
    """
    An abstract base class for Pokemon
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(
        self, stat_max: Statistic = None, stat_current: Statistic = None, level: int = 0, name: str = None, type_pk: str = None
    ):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._stat_max: Statistic = stat_max
        self._stat_current: Statistic = stat_current
        self._level: int = level
        self._name: str = name
        self._type: str = type_pk

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns:
            float: the multiplier
        """
        pass

    def level_up(self) -> None:
        """
        Increase the level by one
        """
        self._level += 1

    def reset_actual_stat(self) -> None:
        """
        Reset the current statistics to the maximum statistics.
        """
        self._stat_current = copy.deepcopy(self._stat_max)

    def get_hit(self, damage: int) -> None:
        """
        Decrease health point when receiving damages.

        Args:
            damage (int): The amount of damage received.
        """
        if damage > 0:
            if damage < self.hp_current:
                self.hp_current -= damage
            else:
                self.hp_current = 0

    def is_ko(self) -> bool:
        """
        Check if the Pokemon is KO.

        Returns:
            bool: True if the Pokemon is KO, False otherwise.
        """
        return self.hp_current <= 0

    def __str__(self) -> str:
        res = f"I am {self.name}, level: {self.level}, attack coef: {self.get_pokemon_attack_coef()}"
        return res

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------

    @property
    def attack(self) -> int:
        """Get the maximum attack stat."""
        return self._stat_max.attack

    @property
    def hp(self) -> int:
        """Get the maximum HP stat."""
        return self._stat_max.hp

    @property
    def defense(self) -> int:
        """Get the maximum defense stat."""
        return self._stat_max.defense

    @property
    def sp_atk(self) -> int:
        """Get the maximum special attack stat."""
        return self._stat_max.sp_atk

    @property
    def sp_def(self) -> int:
        """Get the maximum special defense stat."""
        return self._stat_max.sp_def

    @property
    def speed(self) -> int:
        """Get the maximum speed stat."""
        return self._stat_max.speed

    @property
    def attack_current(self) -> int:
        """Get the current attack stat."""
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value: int) -> None:
        """Set the current attack stat."""
        self._stat_current.attack = value

    @property
    def hp_current(self) -> int:
        """Get the current HP stat."""
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value: int) -> None:
        """Set the current HP stat."""
        self._stat_current.hp = value

    @property
    def defense_current(self) -> int:
        """Get the current defense stat."""
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value: int) -> None:
        """Set the current defense stat."""
        self._stat_current.defense = value

    @property
    def sp_atk_current(self) -> int:
        """Get the current special attack stat."""
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value: int) -> None:
        """Set the current special attack stat."""
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self) -> int:
        """Get the current special defense stat."""
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value: int) -> None:
        """Set the current special defense stat."""
        self._stat_current.sp_def = value

    @property
    def speed_current(self) -> int:
        """Get the current speed stat."""
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value: int) -> None:
        """Set the current speed stat."""
        self._stat_current.speed = value

    # Basic Getter / Setter
    @property
    def stat(self) -> Statistic:
        """Get the maximum statistics."""
        return self._stat_max

    @property
    def level(self) -> int:
        """Get the level of the Pokemon."""
        return self._level

    @property
    def name(self) -> str:
        """Get the name of the Pokemon."""
        return self._name

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


class AbstractAttack(ABC):
    """
    An abstract base class for attacks
    """

    def __init__(self, power: int, name: str, description: str):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, attacker: 'AbstractPokemon', defender: 'AbstractPokemon') -> int:
        """
        Compute the damage of the attack.

        Args:
            attacker (AbstractPokemon): The attacking Pokemon.
            defender (AbstractPokemon): The defending Pokemon.

        Returns:
            int: The damage dealt.
        """
        pass

    @property
    def power(self) -> int:
        """Get the power of the attack."""
        return self._power

    @property
    def name(self) -> str:
        """Get the name of the attack."""
        return self._name

    @property
    def description(self) -> str:
        """Get the description of the attack."""
        return self._description


class FixedDamageAttack(AbstractAttack):
    """
    A fixed damage attack
    """

    def compute_damage(self, attacker: 'AbstractPokemon', defender: 'AbstractPokemon') -> int:
        """
        Compute the damage of the fixed damage attack.

        Args:
            attacker (AbstractPokemon): The attacking Pokemon.
            defender (AbstractPokemon): The defending Pokemon.

        Returns:
            int: The damage dealt.
        """
        return self._power


import random


class AbstractFormulaAttack(AbstractAttack, ABC):
    """
    An abstract base class for formula-based attacks
    """

    def __init__(self, power: int, name: str, description: str):
        super().__init__(power, name, description)

    def compute_damage(self, attacker: AbstractPokemon, defender: AbstractPokemon) -> int:
        """
        Compute the damage of the formula-based attack.

        Args:
            attacker (AbstractPokemon): The attacking Pokemon.
            defender (AbstractPokemon): The defending Pokemon.

        Returns:
            int: The damage dealt.
        """
        level = attacker.level
        power = self.power
        att = self.get_attack_stat(attacker)
        defense = self.get_defense_stat(defender)
        random_multiplier = random.uniform(0.85, 1)
        other_multipliers = attacker.get_pokemon_attack_coef()

        damage = (((2 * level / 5 + 2) * power * att) / (defense * 50) + 2) * random_multiplier * other_multipliers
        return int(damage)

    @abstractmethod
    def get_attack_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the attack stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The attack stat.
        """
        pass

    @abstractmethod
    def get_defense_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the defense stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The defense stat.
        """
        pass


class PhysicalAttack(AbstractFormulaAttack):
    """
    A physical attack
    """

    def get_attack_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the attack stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The attack stat.
        """
        return pokemon.attack_current

    def get_defense_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the defense stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The defense stat.
        """
        return pokemon.defense_current

class SpecialAttack(AbstractFormulaAttack):
    """
    A special attack
    """

    def get_attack_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the special attack stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The special attack stat.
        """
        return pokemon.sp_atk_current

    def get_defense_stat(self, pokemon: AbstractPokemon) -> int:
        """
        Get the special defense stat of the Pokemon.

        Args:
            pokemon (AbstractPokemon): The Pokemon.

        Returns:
            int: The special defense stat.
        """
        return pokemon.sp_def_current
