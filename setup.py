import subprocess
import os
import platform

if platform.system() == "Linux":

    # set name of program-directory and the parent folder of the symlink (usually .config or straight in home)
    name = "xinitrc"
    symParDir = "$HOME"

    # set the directory where you want the actual program repository (not the symlink) to be stored
    repoParDir = "$HOME/.dotfileRepos"

    ###

    # create .dotfileRepos directory to store all dotfiles in one spot. symlinks to the correct locations are created at a later step.
    subprocess.run([f"echo creating directory {repoParDir}"], shell=True)
    subprocess.run([f"mkdir {repoParDir}"], shell=True)

    # create the symlink directory
    subprocess.run([f"echo creating directory {symParDir}"], shell=True)
    subprocess.run([f"mkdir {symParDir}"], shell=True)

    # check if script is being executed from the correct directory already or if the folder needs to be moved
    currDir = os.path.dirname(os.path.realpath(__file__))
    print(currDir)
    targetDir = subprocess.run([f"echo {repoParDir}/{name}"], shell=True, capture_output=True, text=True).stdout.strip()
    print(targetDir)
    if currDir != targetDir:
        subprocess.run([f"echo moving directory from {currDir} to {repoParDir}/{name}"], shell=True)
        subprocess.run([f"mv {currDir} {repoParDir}/{name}"], shell=True)

    # create the symlink    
    pathSym = subprocess.run([f"echo {symParDir}/{name}"], shell=True, capture_output=True, text=True).stdout.strip()
    if os.path.islink(pathSym) == False:
        subprocess.run([f"echo creating symlink for {repoParDir}/{name}/{name} {symParDir}/.{name}"], shell=True)
        subprocess.run([f"ln -s {repoParDir}/{name}/{name} {symParDir}/.{name}"], shell=True)
