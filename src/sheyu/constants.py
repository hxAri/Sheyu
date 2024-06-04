#!/usr/bin/env python3

#
# @author hxAri
# @create 24.04-2022
# @update -
# @github https://github.com/hxAri/Sheyu
#
# Copyright (c) 2022 hxAri <hxari@proton.me>
#
# GNU General Public License v3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>
#

from builtins import str as Str
from sys import path as paths
from typing import Final, MutableSequence


BASEPARTS:MutableSequence[Str] = paths[0].split( "\x2f" )
BASEPATH:Final[Str] = "\x2f".join( BASEPARTS[:BASEPARTS.index( "src" )] )
""" The Base Path of Society Application """

BASEPARTS:MutableSequence[Str] = paths[4].split( "\x2f" )
BASEVENV:Final[Str] = "\x2f".join( BASEPARTS[:BASEPARTS.index( "lib" )] )
""" The Base Path of Virtual Environment """

# Delete unused constant.
del BASEPARTS
