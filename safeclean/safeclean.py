#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Information:
#
# ******************************************************************************
# Type: Python Script
# Linux Compatibility: Linux distros
# Description: Script that cleans the trash safely without leaving a trace.
# Script Name: safeclean

# Author: William C. Canin
#   Contacts:
#   E-Mail: william.costa.canin@gmail.com
#   WebSite: https://williamcanin.me
#   GitHub: https://github.com/williamcanin
#   License: MIT.

import os
# # Import for debugging.
# from pdb import set_trace

class SafeClean():

    config = {
        'appname': 'Safeclean',
        'appscript': 'safeclean.py',
        'appversion': '1.0.1',
        'python_version': 3,
        'userhome': os.path.expanduser('~'),
        'dependencies': ['wipe', 'find', 'shred'],
        'author': {
            'name': 'William C. Canin',
            'email': 'william.costa.canin@gmail.com',
            'website': 'https://williamcanin.me',
            'github': 'https://github.com/williamcanin'
        }
    }

    def credits(self):
        """
            Function to show credits.
        """        
        from datetime import date
        print(f"""\033[36m
   ---------------------------------------------------------
  |                 {self.config['appname']} - Version {self.config['appversion']}               |
   ---------------------------------------------------------
  |                         Credits:                        |
  |                                                         |
  |           Author: {self.config['author']['name']}                      |
  |           E-Mail: {self.config['author']['email']}         |
  |           Website: {self.config['author']['website']}              |
  |           GitHub: {self.config['author']['github']}       |
  |           Locale: Brasil - SP                           |
  |                                                         |
  |                                                         |
  |    {self.config['appname']} © 2018-{date.today().year} - All Right Reserved.          |
  |    Doc: http://github.com/williamcanin/safeclean        |
  |---------------------------------------------------------|
        \033[0m""")

    def verify_user(self, uid) -> bool(object):
        """
            Function to check if script is running with superuser.
        """
        from os import geteuid

        if geteuid() == uid:
            print(f'{self.config["appname"]} can not be run with superuser (root). Aborted!')
            return False
        else:
            return True

    def python_version_required(self, p_version) -> bool(object):
        """
            Function to check the version of Python that this script uses.
        """
        import sys
        try:
            if sys.version_info[0] != p_version:
                raise Exception('You are not using a version of Python that the script supports. ' +
                                'Must be using Python {}.'.format(p_version))
                return False
            else:
                return True
        except Exception as err:
            print('Error!', err)

    def verify_dependencies(self) -> bool(object):
        """
            Function to check script dependencies.
        """
        from os.path import isfile

        for item in self.config['dependencies']:
            if not isfile('/usr/bin/' + item):
                raise Exception(f'The following dependencies are missing: {item}')
                return False
                break
            else:
                return True

    def clean(self) -> bool(object):
        from subprocess import check_output

        print('Cleaning the trash can safely ...')
        trash_dir = self.config['userhome'] + '/.local/share/Trash/files/'
        array = ['find ' + trash_dir + ' -depth -type f -exec shred -v -n 4 -z -u {} \;', 
                 'wipe -r -f ' + trash_dir,
                 'mkdir -p ' + trash_dir]
        try:
            for item in array:
                check_output(item, shell=True, universal_newlines=True)
                print('Done!')
            return True
        except Exception as err:
            print('There was an error with the program code !!!', err)
            return False

    def menu(self):
        """
            Function to create menu.
        """
        from argparse import ArgumentParser, RawTextHelpFormatter
        try:
            parser = ArgumentParser(prog=self.config['appname'],
                                    usage=self.config['appscript'] + ' { run | credits }',
                                    description=self.config['appname'] + 'that cleans the trash ' +
                                                'safely without leaving a trace.',
                                    formatter_class=RawTextHelpFormatter,
                                    epilog="See you later!!")
            parser.add_argument('command', action='store', metavar="{ run | credits }",
                                type=str,
                                help=f"""
run          clean the trash safely.
credits      show credits """)
            parser.add_argument('-c', '--close',
                                action='store_const',
                                const="close",
                                metavar="-c, --close",
                                help='clean the trash safely and close the terminal.')
            args = parser.parse_args()
            return args

        except Exception as err:
            print('Error in passing arguments..', err)

    def main(self):
        """
            Function main. Where the logic will be.
        """
        self.python_version_required(3)
        self.verify_user(0)
        self.verify_dependencies()

        if self.menu().command == 'run':
            if self.menu().close != 'close':
                self.clean()
            else:    
                import signal
                self.clean()
                # Close terminal
                os.kill(os.getppid(), signal.SIGHUP)
        elif self.menu().command == 'credits':
            self.credits()

if __name__ == '__main__':
    sc = SafeClean()
    sc.main()
