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

from abc import ABC as Abstract
from builtins import bool as Bool, int as Int, str as Str
from json import dumps as JsonDumper, loads as JsonLoader
from pytz import timezone as TimeZone
from pytz.tzinfo import DstTzInfo
from typing import (
	Any, 
	final, 
	Final, 
	Literal, 
	MutableMapping, 
	MutableSequence, 
	TypeVar as Var, 
	Union 
)
from yaml import (
	safe_dump as YamlDumper,
	safe_load as YamlLoader
)


Dumper = Var( "Dumper", JsonDumper, YamlDumper )
""" Configuration Dumper """

Loader = Var( "Loader", JsonLoader, YamlLoader )
""" Configuration Loader """

class Typing( Abstract ): ...


@final
class Property:
	
	""" Application Property """
	
	@final
	class Pathname( Typing ):
		
		""" Pathname Typing Implementation """
		
		history:Str
		""" Pathname of command history """
		
		logging:Str
		""" Pathname of logging """
		
		def __init__( self, history:Str, logging:Str ) -> None:
			
			"""
			Construct method of class Pathname
			
			:params Str history
			:params Str logging
			
			:return None
			"""
			
			self.history = history
			self.logging = logging
		
		...
	
	@final
	class Prompt( Typing ):
		
		""" Prompt Typing Implementation """
		
		@final
		class DateTime( Typing ):
			
			""" DateTime Typing Implementation """
			
			format:Str
			""" DateTime string format """
			
			timezone:DstTzInfo
			""" DateTime timezone """
			
			def __init__( self, format:Str, timezone:Union[Str,DstTzInfo] ) -> None:
				
				"""
				Construct method of class DateTime
				
				:params Str format
				:params Str|DstTzInfo timezone
				"""
				
				self.format = format
				if isinstance( timezone, Str ):
					timezone = TimeZone( timezone )
				self.timezone = timezone
			
			...
		
		datetime:DateTime
		""" Prompt DateTime condifguration """
		
		formatter:Str
		""" Prompt Formatter """
		
		def __init__( self, datetime:Union[DateTime,MutableMapping[Str,Union[Str,DstTzInfo]]], formatter:Str=None ) -> None:
			
			"""
			Construct method of class Prompt
			
			:params DateTime|MutableMapping<Str,Str|DstTzInfo> datetime
			:params Str formatter
			
			:return None
			"""
			
			if not isinstance( datetime, Property.Prompt.DateTime ):
				datetime = Property.Prompt.DateTime( **datetime )
			self.datetime = datetime
			if formatter is None:
				formatter = "$"
			self.formatter = formatter
		
		def formats( self, server:"Property.Server" ) -> Str:
			...
		
		...
	
	@final
	class Server( Typing ):
		
		""" Server Typing Implementation """
		
		@final
		class Auth( Typing ):
			
			""" Auth Typing Implementation """
			
			username:Str
			""" Server Username """
			
			password:Str
			""" Server Password """
			
			def __init__( self, username:Str, password:Str ) -> None:
				
				"""
				Construct method of class Auth
				
				:params Str username
				:params Str password
				
				:return None
				"""
				
				self.username = username
				self.password = password
			
			...
		
		auth:Auth
		""" Server Authorization Configuration """
		
		host:Str
		""" Server Hostname """
		
		port:Int
		""" Server Portnumber """
		
		type:Literal[ "SFTP", "SSH" ]
		""" Server Type """
		
		def __init__( self, auth:Union[MutableMapping[Literal[ "username", "password" ],Str],Auth], host:Str, port:Int, type:Literal[ "SFTP", "SSH" ] ) -> None:
			
			"""
			Construct method of class Server
			
			:params MutableMapping<Literal<username|password>,Str>|Auth auth
			:params Str host
			:params Int port
			:params Literal<SFTP|SSH> type
			
			:return None
			"""
			
			if not isinstance( auth, Property.Server.Auth ):
				auth = Property.Server.Auth( **auth )
			self.auth = auth
			self.host = host
			self.port = port
			self.type = type
		
		...
	
	colorize:Bool
	""" Automatically colorize the output """
	
	pathname:Pathname
	""" Pathname configuration """
	
	prompt:Prompt
	""" Terminal prompt configuration """
	
	servers:MutableSequence[Server]
	""" MutableSequence of Server """
	
	def __init__( self ) -> None:
		self.colorize = True
		self.history = True
		self.logging = True
		self.pathname = Property.Pathname(
			history="resources/histories",
			logging="resources/logging"
		)
		self.prompt = Property.Prompt(
			datetime=Property.Prompt.DateTime(
				format="%d.%m-%Y %H:%M",
				timezone=TimeZone( "Asia/Tokyo" )
			)
		)
		self.servers = []
		self.welcome = [
			"Welcome to Remote Shell Execution",
			"Enjoy Your Live, Wtf Idk What Happen"
		]
	
	def update( self, **kwargs:Any ) -> None:
		
		"""
		Update property attributes
		
		:params Any **kwargs
		
		:return None
		:raises AttributeError
			Raises when the property does not have attribute want to set
		:raises TypeError
			When the attribute value is invalid value type
			When the attribute want to overwrite is callable
		"""
		
		for item in kwargs.items():
			keyset, value = item
			if hasattr( self, keyset ) is True:
				if callable( getattr( self, keyset ) ) is True:
					raise TypeError( f"Cannot overwrite attribute \"{keyset}\" it is callable" )
				if keyset == "pathname":
					if not isinstance( value, ( MutableMapping, Property.Pathname ) ):
						raise TypeError( f"Invalid value of attribute \"{keyset}\", value must be type MutableMapping<Str,Str>|Property.Pathname" )
					value = Property.Pathname( **value ) if not isinstance( value, Property.Pathname ) else value
				elif keyset == "prompt":
					if not isinstance( value, ( MutableMapping, Property.Prompt ) ):
						raise TypeError( f"Invalid value of attribute \"{keyset}\", value must be type MutableMapping<Str,Str>|Property.Prompt" )
					value = Property.Prompt( **value ) if not isinstance( value, Property.Prompt ) else value
				elif keyset == "servers":
					if not isinstance( value, MutableSequence ) or \
						not all( isinstance( server, ( MutableMapping, Property.Server ) ) for server in value ):
						raise TypeError( f"Invalid value of attribute \"{keyset}\", value must be type MutableSequence<MutableMapping<Str,Int|MutableMapping<Str,Str>|Property.Server.Auth|Str>|Property.Server>" )
					for index, val in enumerate( value ):
						value[index] = Property.Server( **val ) \
							if not isinstance( val, Property.Server ) else val
						...
					...
				elif keyset == "welcome":
					if not isinstance( value, MutableSequence ) or \
					   not all( isinstance( val, Str ) for val in value ):
						raise TypeError( f"Invalid value of attribute \"{keyset}\", value must be type MutableSequence<Str>" )
					...
				...
				setattr( self, keyset, value )
				continue
			raise AttributeError( f"Unknown attribute name \"{keyset}\"" )
		...
	
	def export( self, dumper:Dumper=YamlDumper ) -> Any:
		contents = {}
		contents['colorize'] = self.colorize
		contents['history'] = self.history
		contents['logging'] = self.logging
		contents['pathname'] = {
			"history": self.pathname.history,
			"logging": self.pathname.logging
		}
		contents['prompt'] = {
			"datetime": {
				"format": self.prompt.datetime.format,
				"timezone": self.prompt.datetime.timezone.zone
			},
			"prompt": self.prompt.formatter
		}
		contents['servers'] = list(
			{
				"auth": {
					"username": server.auth.username,
					"password": server.auth.password
				},
				"host": server.host,
				"port": server.port,
				"type": server.type
			} for server in self.servers
		)
		contents['welcome'] = self.welcome
		if dumper is YamlDumper:
			return YamlDumper( contents, indent=4 )
		return JsonDumper( contents, indent=4 )
	
	...


Properties:Final[Property] = Property()
""" Global Application Properties """
