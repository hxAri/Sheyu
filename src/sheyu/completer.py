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
from typing import Any, Dict, Iterable, List

from sheyu.command import Command
from sheyu.parser import Parser


ARGUMENT:int = 0
OPTIONAL:int = 1

class Completer( BaseCompleter ):

	""" Completer Implementation """

	def __init__( self ) -> None:
		self.__registed__:Dict[str,Command] = {
			"echo": Command( **{
				"meta": "[-neE] [arg ...]",
				"name": "echo",
				"pathname": "/usr/bin",
				"execute": "/usr/bin/echo",
				"arguments": None,
				"options": [
					"-e",
					"-E",
					"-n"
				],
				"description": [
				]
			})
		}
		self.__commands__:List[Command] = self.get_executables()
	
	@property
	def commands( self ) -> List[Command]:
		return self.__commands__

	def get_completions( self, document:Document, complete_event:CompleteEvent ) -> Iterable[Completion]:
		textBeforeCursor = document.text_before_cursor
		textBeforeCursorParts = Parser.parse( textBeforeCursor )
		textBeforeCursorPart = textBeforeCursorParts[0]
		del textBeforeCursorParts[0]
		length = - len( textBeforeCursor )
		for command in self.commands:
			if command.name.startswith( textBeforeCursorPart ):
				if complete_event.text_inserted:
					yield Completion( 
						text=command.name, 
						start_position=length, 
						display=f"{command.name}",
						display_meta=command.meta,
						# style="",
						# selected_style=""
					)
				elif complete_event.completion_requested:
					yield Completion( 
						text=f"{command.name}\nxx", 
						start_position=length, 
						display=command.name,
						display_meta=f"{command.meta}\nxxx",
						# style="",
						selected_style="red"
					).__doc__
	
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
					command = file.name.strip()
					execute = file.path
					pathname = dirname( file.path )
					if not command in self.registed:
						results.append( Command( command, pathname, execute ) )
					else:
						self.registed[command].__execute__ = execute
						self.registed[command].__pathname__ = pathname
						results.append( self.registed[command] )
					appends.append( file.name )
				except PermissionError as e:
					pass
			...
		return results
	
	@property
	def registed( self ) -> Dict[str,Command]:
		return self.__registed__
	
	...
