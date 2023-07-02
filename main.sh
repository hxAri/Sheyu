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

# Show System Informations.
function show()
{
	function detectDistro()
	{
		return 0
	}
	function detectKernel()
	{
		return 0
	}
}

# Main Program.
function main()
{
	# Main menu.
	function menu()
	{
		clear
		show
		echo -e ""
		echo -e "1. Change File Mode"
		echo -e "2. Change Current Working Directory"
		echo -e "3. Display List File/Directory"
		echo -e "4. Encrypt or Decrypt File"
		echo -e "5. File Info"
		echo -e "6. Move Directory"
		echo -e "7. "
		echo -e "8. "
		echo -e "9. "
		echo -e "0. Exit"
		echo -e ""
	}
	menu
	while true; do
		if [[ $input != "" ]]; then
			case $input in
				1 )
					break
				;;
				0 )
					exit
				;;
				*)
					echo "Input of range"
				;;
			esac
		fi
		echo -e "\rInput:\x20\c"
		read input
	done
}

# Starting program.
main

# Close program.
exit
