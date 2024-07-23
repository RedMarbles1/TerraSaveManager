#These are variables used in the script. You can edit them accordingly to your liking.
#The directory that the Terraria save directory will be linked to:
linkdir = ""
#Do not edit anything below this line if you don't know what you are doing.

from sys import platform
import os

#Get which os it is running on and the game save folder according to that
saverootdir = "e"
if platform == "linux":
    saverootdir = os.path.expanduser("~/.local/share/")
elif platform == "darwin":
    saverootdir = os.path.expanduser("~/Library/Application Support/TSMTest/")
elif platform == "win32":
    saverootdir = os.path.expanduser("~/Documents/My Games/")

origsavedir = saverootdir + "Terraria_Orig"
gamesavedir = saverootdir + "Terraria"

#woooow actual loading stuff happens
if __name__ == '__main__':
    print("TerraSaveManager 1.0 \n!This tool will not do anything to your steam cloud saves, only local saves will work!")        
    print("WARNING: Please backup your Terraria folder before using this.")
    print("Windows users should run this script as administrator.")
    print("Saves will be linked from "+ linkdir)
    wowuserinput = input("\nChoose one of the options: \n1. Link the save folder to the Terraria save folder. \n2. Revert changes. \n3. Exit. \n")
    match wowuserinput:
        case "1":
            
            a = input(f"Proceed with the linking? This will not overwrite the old saves. Your old saves will be available in {origsavedir}. y/n\n")
            if a == "y" or "yes":
                if not os.path.isdir(origsavedir):
                    os.rename(gamesavedir, origsavedir)
                try: 
                    os.remove(gamesavedir)
                    os.symlink(linkdir,gamesavedir)
                except FileExistsError:
                    print("Something seems to be wrong with the files! Check if the source directory exists and there isn't anything with the name \"Terraria\" on the target directory.")
                    exit()
                except OSError:
                    print("Linking failed! Try running this script as administrator.")
                    exit()
                print("Done!")
                exit()
            else:
                print("Confirmation declined, exiting!")
                exit()
        case "2":
            b = input(f"This will remove the link and restore your old Terraria saves in {origsavedir}. Proceed? y/n\n")
            if b == "y" or "yes":
                try:
                    os.rmdir(gamesavedir)
                except FileNotFoundError:
                    print("The link seems to be deleted before you ran this program but we will keep going anyway to restore your data back.")
                os.rename(origsavedir, gamesavedir)
                print("Done!")
                exit()
            else:
                print("Confirmation declined, exiting!")
                exit()
        case "3":
                print("Exiting!")
                exit()