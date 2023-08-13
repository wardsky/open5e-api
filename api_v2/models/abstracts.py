"""
The model for an object.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify


class HasName(models.Model):

    name = models.CharField(
        max_length=100,
        help_text='Name of the item.')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class HasDescription(models.Model):
    desc = models.TextField(
        help_text='Description of the game content item. Markdown.')

    class Meta:
        abstract = True


class Localized(models.Model):

    key = models.CharField(
        primary_key=True,
        max_length=100,
        help_text="Unique key for the localized content.")
    lang = models.TextField(
        help_text='What language this content is written in, e.g., "en" or "fr".')

    class Meta:
        abstract = True


class Object(models.Model):
    """
    This is the definition of the Object abstract base class.

    The Object class will be inherited from by Item, Weapon, Character, etc.
    Basically it describes any sort of matter in the 5e world.
    """

    # Enumerating sizes, so they are sortable.
    SIZE_CHOICES = [
        (1, "Tiny"),
        (2, "Small"),
        (3, "Medium"),
        (4, "Large"),
        (5, "Huge"),
        (6, "Gargantuan")]

    # Setting a reasonable maximum for AC.
    ARMOR_CLASS_MAXIMUM = 100

    # Setting a reasonable maximum for HP.
    HIT_POINT_MAXIMUM = 10000

    size = models.IntegerField(
        default=1,
        null=False,  # Allow an unspecified size.
        choices=SIZE_CHOICES,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)],
        help_text='Integer representing the size of the object.')

    weight = models.DecimalField(
        default=0,
        null=False,  # Allow an unspecified weight.
        max_digits=10,
        decimal_places=3,
        validators=[MinValueValidator(0)],
        help_text='Number representing the weight of the object.')

    armor_class = models.IntegerField(
        default=0,
        null=False,  # Allow an unspecified armor_class.
        validators=[
            MinValueValidator(0),
            MaxValueValidator(ARMOR_CLASS_MAXIMUM)],
        help_text='Integer representing the armor class of the object.')

    hit_points = models.IntegerField(
        default=0,
        null=False,  # Allow an unspecified hit point value.
        validators=[
            MinValueValidator(0),
            MaxValueValidator(HIT_POINT_MAXIMUM)],
        help_text='Integer representing the hit points of the object.')

    class Meta:
        abstract = True
        ordering = ['pk']
