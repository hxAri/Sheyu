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

from builtins import bool as Bool, int as Int, str as Str
from datetime import datetime
from io import TextIOWrapper
from json import dumps as encoder
from mimetypes import guess_type as mimetype
from os import makedirs as mkdir, path
from typing import Any, MutableSequence, Union

from sheyu.constants import BASEPATH


class Storage:
	
	""" Storage Class Implementation """
	
	@staticmethod
	def fname() -> Str: return datetime.now().strftime( "%Y-%m-%d %H:%M:%S.json" )
	
	@staticmethod
	def cat( fname:Str, fmode:Str="r", encoding:Str=None, stream:Bool=False ) -> Union[Str,TextIOWrapper]:
		
		"""
		Read the file contents
		
		:params Str fname
			The filename want to be read
		:params Str fmode
			The file read mode
		:params Str encoding
			The file encoding
		:params Bool stream
			Only return the wrapper
		
		:return Str|TextIOWrapper
		"""
		
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		if stream is True:
			return open( fname, fmode, encoding=encoding )
		with open( fname, fmode, encoding=encoding ) as fopen:
			fread = fopen.read()
			fopen.close()
		return fread
	
	@staticmethod
	def catln( fname:Str, fmode:Str="r", encoding:Str=None ) -> MutableSequence[Str]:
		
		"""
		Read file and split file contents with new line
		
		:params Str fname
			The filename want to be read
		:params Str fmode
			The file read mode
		:params Str encoding
			The file encoding
		
		:return MutableSequence<Str>
		"""
		
		return Storage.cat( fname, fmode=fmode, encoding=encoding ).splitlines()
	
	@staticmethod
	def d( dname:Str ) -> Bool:
		if dname[0] != "\x2f":
			dname = f"{BASEPATH}/{dname}"
		return path.isdir( dname )
	
	@staticmethod
	def f( fname:Str ) -> Bool:
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		return path.isfile( fname )
	
	@staticmethod
	def mime( fname:Str ) -> Str:
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		return mimetype( fname )[0]
	
	@staticmethod
	def mkdir( dname:Str, mode:Int=511, existOk:Bool=True ) -> None:
		
		"""
		Make new directory
		
		:params Str dname
			The directory target
		:params Int mode
		:params Bool existOk
		
		:return None
		"""
		
		if dname[0] != "\x2f":
			dname = f"{BASEPATH}/{dname}"
		mkdir( dname, mode=mode, exist_ok=existOk )
	
	@staticmethod
	def touch( fname:Str, data:Any, fmode:Str="w", encoding:Str=None ) -> None:
		
		"""
		Create or append file contents.
		
		:params Str fname
		:params Any data
		:params Str fmode
		:params Str encoding
			The file encoding
		
		:return None
		"""
		
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		with open( fname, fmode, encoding=encoding ) as fopen:
			fdata = data
			if not isinstance( data, ( Str, bytes ) ):
				try:
					fdata = encoder( data, indent=4 )
				except BaseException:
					fdata = str( data )
			fopen.write( fdata )
			fopen.close()
		...
	
	...
