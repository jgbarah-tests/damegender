#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# This class is used to operations between all methods/apis

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_genderize import DameGenderize
from app.dame_genderapi import DameGenderApi
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser

class DameAll(Gender):
    def average(self, name, surname):
        r = 0
        count = 0
        dgg = DameGenderGuesser()
        guess1 = dgg.guess(name, binary="True")
#        print(guess1)
        if (guess1 != 2):
            r = r + guess1
            count = count +1
        dga = DameGenderApi()
        guess2 = dga.guess(name, binary="True")
        if (guess2 != 2):
            r = r + guess2
            count = count +1
#        print(guess2)
        dg = DameGenderize()
        guess3 = dg.guess(name, binary="True")
        if (guess3 != 2):
            r = r + guess3
            count = count +1
#        print(guess3)
        dn = DameNamsor()
        guess4 = dn.guess(str(name), str(surname), binary="True")
        if (guess4 != 2):
            r = r + guess4
            count = count +1
#        print(guess4)
        avg = r / count
        return avg