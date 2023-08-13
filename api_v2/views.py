from django.db.models import Subquery, OuterRef
from django_filters import FilterSet
from django_filters import BooleanFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import viewsets

from api_v2 import models
from api_v2 import serializers
from api.schema_generator import CustomSchema


class ItemFilterSet(FilterSet):
    is_magic_item = BooleanFilter(field_name='rarity', lookup_expr='isnull', exclude=True)

    class Meta:
        model = models.Item
        fields = {
            'key': ['in', 'iexact', 'exact' ],
            'cost': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'weight': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'rarity': ['exact', 'in', ],
            'requires_attunement': ['exact'],
            'category': ['in', 'iexact', 'exact'],
            'document__key': ['in','iexact','exact']
        }


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of items.

    retrieve: API endpoint for returning a particular item.
    """
    text_queryset = models.ItemText.objects.filter(
        item=OuterRef('pk'),
        lang='en',
    )
    queryset = models.Item.objects.annotate(
        name=Subquery(text_queryset.values('name')[:1]),
        desc=Subquery(text_queryset.values('desc')[:1]),
    ).order_by('pk')
    serializer_class = serializers.ItemSerializer
    filterset_class = ItemFilterSet


class ItemSetFilterSet(FilterSet):

    class Meta:
        model = models.ItemSet
        fields = {
            'key': ['in', 'iexact', 'exact' ],
            'name': ['iexact', 'exact'],
            'document__key': ['in','iexact','exact']
        }


class ItemSetViewSet(viewsets.ReadOnlyModelViewSet):
    """"
    list: API Endpoint for returning a set of itemsets.

    retrieve: API endpoint for return a particular itemset.
    """
    queryset = models.ItemSet.objects.all().order_by('pk')
    serializer_class = serializers.ItemSetSerializer
    filterset_class = ItemSetFilterSet


class RulesetViewSet(viewsets.ReadOnlyModelViewSet):
    """"
    list: API Endpoint for returning a set of rulesets.

    retrieve: API endpoint for return a particular ruleset.
    """
    queryset = models.Ruleset.objects.all().order_by('pk')
    serializer_class = serializers.RulesetSerializer


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of documents.
    retrieve: API endpoint for returning a particular document.
    """
    queryset = models.Document.objects.all().order_by('pk')
    serializer_class = serializers.DocumentSerializer
    filterset_fields = '__all__'


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of publishers.
    retrieve: API endpoint for returning a particular publisher.
    """
    queryset = models.Publisher.objects.all().order_by('pk')
    serializer_class = serializers.PublisherSerializer
    filterset_fields = '__all__'


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of licenses.
    retrieve: API endpoint for returning a particular license.
    """
    queryset = models.License.objects.all().order_by('pk')
    serializer_class = serializers.LicenseSerializer
    filterset_fields = '__all__'


class WeaponFilterSet(FilterSet):

    class Meta:
        model = models.Weapon
        fields = {
            'key': ['in', 'iexact', 'exact' ],
            'document__key': ['in','iexact','exact'],
            'damage_type': ['in','iexact','exact'],
            'damage_dice': ['in','iexact','exact'],
            'versatile_dice': ['in','iexact','exact'],
            'range_reach': ['exact','lt','lte','gt','gte'],
            'range_normal': ['exact','lt','lte','gt','gte'],
            'range_long': ['exact','lt','lte','gt','gte'],
            'is_finesse': ['exact'],
            'is_thrown': ['exact'],
            'is_two_handed': ['exact'],
            'requires_ammunition': ['exact'],
            'requires_loading': ['exact'],
            'is_heavy': ['exact'],
            'is_light': ['exact'],
            'is_lance': ['exact'],
            'is_net': ['exact'],
            'is_simple': ['exact'],
            'is_improvised': ['exact']
            }


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of weapons.
    retrieve: API endpoint for returning a particular weapon.
    """
    text_queryset = models.WeaponText.objects.filter(
        weapon=OuterRef('pk'),
        lang='en',
    )
    queryset = models.Weapon.objects.annotate(
        name=Subquery(text_queryset.values('name')[:1]),
    ).order_by('pk')
    serializer_class = serializers.WeaponSerializer
    filterset_class = WeaponFilterSet


class ArmorFilterSet(FilterSet):

    class Meta:
        model = models.Armor
        fields = {
            'key': ['in', 'iexact', 'exact' ],
            'document__key': ['in','iexact','exact'],
            'grants_stealth_disadvantage': ['exact'],
            'strength_score_required': ['exact','lt','lte','gt','gte'],
            'ac_base': ['exact','lt','lte','gt','gte'],
            'ac_add_dexmod': ['exact'],
            'ac_cap_dexmod': ['exact'],

        }


class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of armor.
    retrieve: API endpoint for returning a particular armor.
    """
    text_queryset = models.ArmorText.objects.filter(
        armor=OuterRef('pk'),
        lang='en',
    )
    queryset = models.Armor.objects.all().annotate(
        name=Subquery(text_queryset.values('name')[:1]),
    ).order_by('pk')
    serializer_class = serializers.ArmorSerializer
    filterset_class = ArmorFilterSet
