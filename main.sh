#!/usr/bin/env bash

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

# Author Information
AUTHOR=hxAri
AUTHOR_NAME=Ari_Setiawan
AUTHOR_EMAIL=hxari@proton.me

# Version Number
VERSION=1.0.2

# System Input.
function input()
{
	while true; do
		if [[ $1 != "" ]]; then
			echo -e "$1:\x20\c"
		else
			echo -e "Input:\x20\c"
		fi
		read inputs
		if [[ $inputs != "" ]]; then
			break
		fi
	done
	echo $inputs
}

# Main Program.
function main()
{
	# ...
	function menu()
	{
		input "input"
	}
	menu
	return 0
}

# Starting program.
main

# Close program.
exit
