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

from prompt_toolkit import PromptSession
from subprocess import run as Subprocess, getoutput
from typing import Literal

from sheyu.completer import Completer


class Sheyu:

	def __init__( self ) -> None:
		self.__completer__:Completer = Completer()
		self.__session__:PromptSession = PromptSession(
			completer=self.completer
		)
	
	@property
	def session( self ) -> PromptSession:
		return self.__session__
	
	@property
	def completer( self ) -> Completer:
		return self.__completer__
	
	...
