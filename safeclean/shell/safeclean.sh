#!/usr/bin/env bash
#
# Information:
#
# ******************************************************************************
# Type: Shell Script
# Linux Compatibility: Linux distros
# Description: Script that cleans the trash safely without leaving a trace.
# Script Name: safeclean

# Author: William C. Canin
#   Contacts:
#   E-Mail: william.costa.canin@gmail.com
#   WebSite: https://williamcanin.github.io
#   GitHub: https://github.com/williamcanin
#   License: MIT.

# Add paths.
PATH=$PATH:/usr/bin:/bin:/usr/sbin:/sbin:/usr/bin/X11
export PATH

# Variables.
TRASH_DIR="$HOME/.local/share/Trash/files/"
# DEP=("wipe")

# # DEPRECATED - Verify distribution Linux. [Archlinux]
# if [[ -f "/etc/os-release" ]]; then
#     distro=$(cat /etc/os-release | grep ^NAME | cut -d"=" -f2 | cut -d"\"" -f2)
#     if [[ "${distro}" != "Arch Linux" ]]; then
#       printf "This distribution Linux is not compatible. \n"
#       exit 1
#     fi
# fi

# DEPRECATED - Verify dependencies. [Archlinux]
# if [[ ! -n $(pacman -Qq ${DEP[@]}) ]]; then
#     printf "This script depends on some packages installed. See the ones that are missing and install. Exit."
#     exit 1
# fi

if [[ ! -f "/usr/bin/wipe" ]]; then
    printf "This script depends on some packages installed. See the ones that are missing and install. Exit."
    exit 1
fi

# Usage print.
_usage() {
  cat <<-EOF

Usage: safeclean [command] [options]

  Command:

    start                Clean the trash safely.

  Options:

    -c, --close          Clean the trash safely and close the terminal.

EOF
}

# Start safeclean.
_safeclean(){
    printf "Cleaning the trash can safely ...\n"

    ### The command line below, depends on shred, which usually comes installed
    ### on most Linux distributions.
    ### NOTE: This feature does not delete the folders, only the files contained in them.
    find ${TRASH_DIR} -depth -type f -exec shred -v -n 4 -z -u {} \;

    ### Removing the Trash Folder [with Wipe].
    wipe -r -d -f -I -v ${TRASH_DIR}
    ### Removing the Trash Folder [with Secure Delete]. Install: yay -S secure-delete.
    # srm -rvz ${TRASH_DIR}

    # Rebuilding the Trash Folder.
    mkdir -p ${TRASH_DIR}

    printf "Done!\n"
}

# Menu
case $1 in
    start)
        if [ -z $2 ]; then
            _safeclean
        else
            case $2 in
                -c|--close) _safeclean; kill -9 $PPID ;;
                *) printf "\nInvalid option! Nothing was accomplished.\n" ;;
            esac
        fi
    ;;
    -h|--help) _usage ;;
    *) printf "\nInvalid command! Nothing was accomplished.\n"; _usage ;;
esac
exit
