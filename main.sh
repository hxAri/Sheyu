#!/usr/bin/env bash

# @author hxAri
# @create 24.04-2022
# @update -
# @github https://github.com/hxAri
#
# Copyright (c) 2022 hxAri <ari160824@gmail.com>
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

clear

declare -a ERRORS
declare -a VERSION
declare -a ARGUMENTS
declare -a POSITIONAL

# Version level
VERSION[${#VERSION[@]}]="v1"

# Version number
VERSION[${#VERSION[@]}]=".0"
VERSION[${#VERSION[@]}]=".1"

# Project license
LICENCE="GPL"
LICENSE_YEAR=2022
LICENSE_AUTHOR="hxAri"

# User Signin
LOGIN=1

# Default user credential
USERNAME=
PASSWORD=

# Disable color
DISABLE_COLOR=0

# Get directory source from file.
target() {
    echo $( dirname "$BASH_SOURCE" )/$1
}

# Change file mode permissions.
chmode() {
    if [[ -f $( target $1 ) ]]; then
        
        # Get file mode permission.
        mode=$( stat -c %a $( target $1 ) )
        
        if [[ $mode == 600 ]]; then
            chmod +x $( target $1 )
        elif [[ $mode < 600 ]]; then
            ERRORS[${#ERRORS[@]}]="Permission denied failed execute $1"
        else
            ERRORS[${#ERRORS[@]}]="Permission has been granted for $1"
        fi
    else
        ERRORS[${#ERRORS[@]}]="Error file $1 not found!"
    fi
}

# Get color.
color() {
    if [[ "$1" ]]; then
        if [[ ${BASH_VERSINFO[0]} -ge 4 ]]; then
            if [[ ${BASH_VERSINFO[0]} -eq 4 && ${BASH_VERSINFO[1]} -gt 1 ]] || [[ ${BASH_VERSINFO[0]} -gt 4 ]]; then
                localTmp=${1,,}
            else
                localTmp="$( tr '[:upper:]' '[:lower:]' <<< "${1}" )"
            fi
        else
            localTmp="$( tr '[:upper:]' '[:lower:]' <<< "${1}" )"
        fi
        if [[ "$2" ]]; then
            if [[ "$localTmp" ]]; then
                case ${localTmp} in
                    "reset" )
                        col="\033[0m\033[$2m"
                    ;;
                    "black" | "gray" )
                        col="\033[0m\033[$2;30m"
                    ;;
                    "red" )
                        col="\033[0m\033[$2;31m"
                    ;;
                    "green" )
                        col="\033[0m\033[$2;32m"
                    ;;
                    "yellow" )
                        col="\033[0m\033[$2;33m"
                    ;;
                    "blue" )
                        col="\033[0m\033[$2;34m"
                    ;;
                    "purple" )
                        col="\033[0m\033[$2;35m"
                    ;;
                    "cyan" )
                        col="\033[0m\033[$2;36m"
                    ;;
                    "white" )
                        col="\033[0m\033[$2;37m"
                    ;;
                    "orange" )
                        case $2 in
                            0 ) col="\033[0m\033[38;5;202m";;
                            1 ) col="\033[0m\033[38;5;214m";;
                        esac
                    ;;
                    "blackHaiku" )
                        col="\033[0m\033[38;5;7m"
                    ;;
                    "rosaBlue" )
                        col="\033[01;38;05;25m"
                    ;;
                    "arcoBlue" )
                        col="\033[01;38;05;111m"
                    ;;
                esac
                if [[ "$col" ]]; then
                    echo "$col"
                fi
            fi
        fi
    fi
}

# Get option list.
option() {
    echo 0
}

# Get ascii logo.
ascii() {
    if [[ "$DISABLE_COLOR" == 0 ]]; then
        
        # Reset Color
        c0=$( color "reset" 0 )
        c1=$( color "reset" 1 )
        
        # Dark Colors
        c00=$( color "black" 0 )
        c01=$( color "red" 0 )
        c02=$( color "green" 0 )
        c03=$( color "yellow" 0 )
        c04=$( color "blue" 0 )
        c05=$( color "purple" 0 )
        c06=$( color "cyan" 0 )
        c07=$( color "white" 0 )
        
        # Light Colors
        c10=$( color "black" 1 )
        c11=$( color "red" 1 )
        c12=$( color "green" 1 )
        c13=$( color "yellow" 1 )
        c14=$( color "blue" 1 )
        c15=$( color "purple" 1 )
        c16=$( color "cyan" 1 )
        c17=$( color "white" 1 )
        
        # Orange colors
        c20=$( color "orange" 0 )
        c21=$( color "orange" 1 )
        
    fi
    case $1 in
        "border" )
            logo=(
                "${c17}                   ::                             "
                "${c17}                  ~JJ^... :~^                     "
                "${c17}            .^::~7JJJJJJ??JJJ^                    "
                "${c17}            7JJJYYJ?77??JJJJJJ?!!??:              "
                "${c17}            :JJJ?^.     .^!?JJJJJJ?.              "
                "${c17}          :^?JJJ.    ~7^   .~?JJJJJ?: ..          "
                "${c17}         .?JJJJJ^  .!JY7     .?JJJJ~::^::.        "
                "${c17}          ..^?JJJ??JJJJ:      :JJJ7.:~!~::.       "
                "${c17}             :JJJ?J?7JJ~       7JJ?^:::::.        "
                "${c17}             .!7^..  :^.       ?JJ?!!~~^          "
                "${c17}                              :JJJ7!!!!!          "
                "${c17}                             .?JJ?!!!~~~.         "
                "${c17}                            ^?JJ?!!^:::::.        "
                "${c17}                          :7JJJ7!!~.:~!~::.       "
                "${c17}                        .!JJJJ7!!!!^::^::.        "
                "${c17}                      .~JJJJJ7!!!!!!!^ .          "
                "${c17}                     ^?JJJJ?!!!!!!!!^             "
                "${c17}                   :7JJJJJ?!!!~^^:^^              "
                "${c17}                 .!JJJJJJ7!!!^::~~::.             "
                "${c17}                ~?JJJJJJ7!!!!^.^!!^:.             "
                "${c17}              ^?JJJJJJJ7!!!!!!^:::..              "
                "${c17}            :7JJJJJJJ?!!!!!!!!^                   "
                "${c17}            7JJJJJJJ?!!!!!!!~:                    "
                "${c17}            .:::::::........                      "
            )
        ;;
        "distro" )
            case $2 in
            esac
        ;;
        "license" )
            case $2 in
                "GNU" | "GPL" )
                    logo=(
                        "${c17}   ********  ****     ** **     **      "
                        "${c17}   **${c10}//////${c17}**${c10}/${c17}**${c10}/${c17}**   ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**     "
                        "${c17}   **      ${c10}// /${c17}**${c10}//${c17}**  ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c10}   /${c17}**         ${c10}/${c17}** ${c10}//${c17}** ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**   "
                        "${c10}   /${c17}**    *****${c10}/${c17}**  ${c10}//${c17}**${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**   "
                        "${c10}   //${c17}**  ${c10}////${c17}**${c10}/${c17}**   ${c10}//${c17}****${c10}/${c17}**    ${c10}/${c17}**   "
                        "${c10}   //${c17}******** ${c10}/${c17}**    ${c10}//${c17}***${c10}//${c17}*******     "
                        "${c10}   ////////  //      ///  ///////       "
                        "${c10}                                        "
                        "${c17}   GNU General Public Licence           "
                        "${c17}   Version 3${c10},${c17} 29 June 2009              "
                        "${c17}                                        "
                        "${c17}   Copyright (c) ${YEAR} ${c10}${AUTHOR}      "
                    )
                ;;
                "MIT" )
                    logo=(
                        "${c17}   ****     **** ** ********** "
                        "${c17}   ${c10}/${c17}**${c10}/${c17}**   **${c10}/${c17}**${c10}/${c17}**${c10}/////${c17}**${c10}/// "
                        "${c17}   ${c10}/${c17}**${c10}//${c17}** ** ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c17}   ${c10}/${c17}** ${c10}//${c17}***  ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c17}   ${c10}/${c17}**  ${c10}//${c17}*   ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c17}   ${c10}/${c17}**   ${c10}/    ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c17}   ${c10}/${c17}**        ${c10}/${c17}**${c10}/${c17}**    ${c10}/${c17}**    "
                        "${c17}   ${c10}//         // //     //     "
                    )
                ;;
            esac
        ;;
    esac
    clear
    if [[ "${logo}" ]]; then
        echo
        for (( i=0; i<${#logo[@]}; i++ )); do
            printf "${logo[$i]}${c07}\n" ""
        done
    fi
}

usage() {
    ascii "usage"
}

input() {
    if [[ "$1" ]]; then
        case $1 in
            "main" )
                ascii "border"
                lists=( # ${c11}
                    "${c0}"
                    "${c0}   1${c11} => ${c17}"
                    "${c0}   2${c11} => ${c17}"
                    "${c0}   3${c20} => ${c17}"
                    "${c0}   4${c20} => ${c17}"
                    "${c0}   5${c20} => ${c17}"
                    "${c0}   6${c21} => ${c17}"
                    "${c0}   7${c21} => ${c17}"
                    "${c0}   8${c21} => ${c17}"
                    "${c0}   9${c13} => ${c17}"
                    "${c0}   0${c13} => ${c17}Exit"
                    "${c0}"
                )
                for list in "${lists[@]}"; do
                    printf "${list}\n"
                done
                printf "   "
                printf ">> "
                read systemIn
                if [[ $systemIn != "" ]]; then
                    case $systemIn in
                        0 )
                            printf ""
                        ;;
                        * )
                            input "main"
                        ;;
                    esac
                else
                    input "main"
                fi
            ;;
            * )
                ERRORS[${#ERRORS[@]}]="Input error, no match for $1"
            ;;
        esac
    else
        ERRORS[${#ERRORS[@]}]="Input parameter error."
    fi
}

# User login.
login() {
    echo 0
}

# Main program.
main() {
    
    input "main"
    input
    
    if [[ "${ERRORS}" ]]; then
        echo
        for i in "${ERRORS[@]}"; do
            echo -e "   $i"
        done
        echo
    fi
}

# Starting program.
main

# Close program.
exit 0
