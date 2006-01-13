# -*- Mode: Python; coding: iso-8859-1 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Stoqdrivers
## Copyright (C) 2005 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
## USA.
##
## Author(s):   Henrique Romano  <henrique@async.com.br>
##
##
"""
stoqdrivers/devices/scales/interface.py:

    Printer Driver API
"""

from zope.interface import Interface, Attribute

class IScaleInfo(Interface):
    """ This interface list the data that read by the scale
    """
    weight = Attribute("The weight read")
    price_per_kg = Attribute("The KG read")
    total_price = Attribute("The total price. It is equivalent to "
                            "price_per_kg * weight")
    code = Attribute("The product code")

class IScale(Interface):
    """ This interface describes how to interacts with scales.
    """

    def read_data():
        """ Read informations of the scale, returning an object
        that implements IScaleInfo interface.
        """