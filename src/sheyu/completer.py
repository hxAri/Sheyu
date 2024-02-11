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

from os import access, scandir, system, X_OK as EXECUTABLE
from os.path import dirname
from prompt_toolkit.completion import (
	CompleteEvent, 
	Completer as BaseCompleter, 
	Completion
)
from prompt_toolkit.document import Document
from subprocess import getoutput
from typing import Iterable, List

from sheyu.command import Command
from sheyu.parser import Parser


class Completer( BaseCompleter ):

	""" Completer Implementation """

	def __init__( self ) -> None:
		self.__commands__:List[Command] = self.get_executables()
	
	@property
	def commands( self ) -> List[Command]:
		return self.__commands__

	def get_completions( self, document:Document, complete_event:CompleteEvent ) -> Iterable[Completion]:
		textBeforeCursor = document.text_before_cursor
		textBeforeCursorParts = textBeforeCursor.split( "\x20" )
		textBeforeCursorPart = textBeforeCursorParts[0]
		del textBeforeCursorParts[0]
		textBeforeCursorJoin = "\x20".join( textBeforeCursorParts )
		for command in self.commands:
			if command.name.startswith( textBeforeCursorPart ):
				if len( textBeforeCursorParts ) >= 1:
					for option in [ "-e", "-E", "-n" ]:
						if option.startswith( textBeforeCursorJoin ):
							yield Completion( text=f"{command.name} {option}", start_position=-len( textBeforeCursor ), display_meta=command.path )
				else:
					yield Completion( text=command.name, start_position=-len( textBeforeCursor ), display_meta=command.path )
	
	def get_executables( self ) -> List[Command]:

		"""
		Return all executable commands

		:return List<Command>
		"""

		results = []
		appends = []
		stdout = getoutput( "echo $PATH" )
		paths = stdout.split( ":" )
		for path in paths:
			files = scandir( path )
			for file in files:
				try:
					if file.name in appends:
						continue
					if not file.is_file():
						continue
					if not access( file.path, EXECUTABLE ):
						continue
					appends.append( file.name )
					results.append( Command(
						file.name,
						dirname( file.path ),
						file.path
					))
				except PermissionError as e:
					pass
			...
		return results
	
	...
