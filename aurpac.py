## AURPAC: Simple AUR helper in Python
## vesrion 1.0

import os
import sys
#import modules

#change to home directory to ensure packages arent cloned in the binary's folder
user = os.getlogin()
os.chdir(f"/home/{user}")


#get the pkg from the args
try:
    targetpkg = str(sys.argv[1]) #store command line arg
    print(f"Package to install: {targetpkg}")

except:
    print("You did not provide a package to install.")
    sys.exit()

#clone the repo from the AUR using git
try:
    os.system(f"git clone https://aur.archlinux.org/{targetpkg}.git")
except:
    print("Something went wrong. You may not have git installed. The AUR may be down or the package may not exist. Try again.")
    sys.exit()

# move to the pkg directory
try:
    wdir = os.getcwd()
    print(wdir)
    os.chdir(f"{wdir}/{targetpkg}")
except:
    print(f"fatal error: no directory was made for {targetpkg}.")
    sys.exit()

# install it
try:
    os.system("makepkg -si")
except:
    print("Something went wrong. try again.")
    sys.exit
