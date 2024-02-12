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

from typing import final, List


@final
class Command:
	
	def __init__( self, name:str, pathname:str, execute:str, arguments:List[str]=None, options:List[str]=None, description:List[str]=None, meta:str=None ) -> None:
		self.__meta__:str = meta
		self.__name__:str = name 
		self.__pathname__:str = pathname
		self.__execute__:str = execute
		self.__arguments__:List[str] = arguments
		self.__options__:List[str] = options
		self.__description__:List[str] = description 

	@property
	def meta( self ) -> str:
		return self.__meta__
	
	@property
	def name( self ) -> str:
		return self.__name__
	
	@property
	def execute( self ) -> str:
		return self.__execute__
	
	@property
	def pathname( self ) -> str:
		return self.__pathname__
	
	@property
	def arguments( self ) -> List[str]:
		return self.__arguments__
	
	@property
	def options( self ) -> List[str]:
		return self.__options__

	@property
	def description( self ) -> List[str]:
		return self.__description__

	...
