#!/usr/bin/env python
#
# pyLOM - Python Low Order Modeling.
#
# POD Module
#
# Last rev: 09/07/2021

__VERSION__ = '1.0.0'

from .wrapper import run, PSD
from .wrapper import temporal_mean, subtract_mean, svd, power_spectral_density

del wrapper