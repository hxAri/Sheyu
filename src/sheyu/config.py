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
from json import dumps as JsonDumper, loads as JsonLoader
from typing import final, Final
from yaml import (
	safe_dump as YamlDumper,
	safe_load as YamlLoader
)

from sheyu.storage import Storage
from sheyu.property import Dumper, Loader, Properties


@final
class Config:
	
	""" The Sheyu Configuration """
	
	Filename:Final[Str] = "properties"
	""" Configuration filename """
	
	@staticmethod
	def load( loader:Loader=YamlLoader ) -> None:
		contents = {}
		if loader is JsonLoader:
			contents = JsonLoader( Storage.cat( f"{Config.Filename}.json" ) )
		elif loader is YamlLoader:
			stream = Storage.cat( f"{Config.Filename}.yaml", stream=True )
			contents = YamlLoader( stream )
		Properties.update( **contents )
	
	@staticmethod
	def save( dumper:Dumper=YamlDumper ) -> None:
		contents = Properties.export( dumper )
		filename = f"{Config.Filename}.yaml"
		if dumper is JsonDumper:
			filename = f"{Config.Filename}.json"
		Storage.touch( filename, contents )
	
	...
