"""
The initialization for models for open5e's api v2.
"""

from .abstracts import HasName
from .abstracts import HasDescription
from .abstracts import Object

from .item import Item
from .item import ItemText
from .item import ItemSet

from .armor import Armor
from .armor import ArmorText

from .weapon import Weapon
from .weapon import WeaponText

from .document import Document
from .document import License
from .document import Publisher
from .document import Ruleset
from .document import FromDocument
