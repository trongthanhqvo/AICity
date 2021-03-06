from __future__ import absolute_import

from .oim import oim, OIM, OIMLoss
from .triplet import TripletLoss
from .npair import NPairLoss, NPairAngularLoss, BatchHardLoss
from .dualmatch import DualMatch, DualMatchTest, MultiPartNPairLoss 
from .crossentropylabelsmooth import CrossEntropyLabelSmooth
from .multi_attribute_loss import MultiAttributeLoss, TypeAttributeLoss

__all__ = [
    'oim',
    'OIM',
    'OIMLoss',
    'TripletLoss',
    'NPairLoss',
    'NPairAngularLoss',
    'BatchHardLoss',
    'DualMatch',
    'DualMatchTest',
    'MultiPartNPairLoss',
    'CrossEntropyLabelSmooth',
    'MultiAttributeLoss'
    'TypeAttributeLoss'
]
