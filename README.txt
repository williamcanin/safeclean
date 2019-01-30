# Safeclean

[ ABOUT ]

  Safeclean is a simple script for Arch Linux with the function of 
    removing the trash in a safe way, with no chance of recovering files.

[ VERSION ]

  Current: 1.0.1

[ DEPENDENCIES ]

  * Linux System
  * wipe
  * shred

[ INSTALL ]

 # make install

[UNINSTALL]

  # make uninstall
 
[ USAGE ]

  For information on how to use it, run the command below:

  $ safeclean -h

[ DEVELOPER ]

  Preparing machine for development:

  A - Create a virtual machine:

   $ git clone https://github.com/williamcanin/safeclean.git; cd safeclean
   $ python3 -m env

  B - Enable virtual machine:

   $ . env/bin/activate

  Tests:

  The file to run tests can be found in the "tests" folder. The file
  "runtests.sh" will run the "Recover Grub" tests (script/recover_grub.py).
  
  The Python module used for testing is the **unittest**.

  Deploy:

  The file ".deploy.git" is a simple shell script to perform the deploy and merge of this project. It's intuitive.

[ LICENSE ]

  MIT License (MIT)
  https://opensource.org/licenses/MIT


 © Safeclean. William C. Canin. All rights reserved. ®
