# REQUIREMENTS:
# 
# 1) Copy all addon packs in the "src" folder to the development pack folders
#    in the minecraft 'com.mojang' folder.
# 2) Run Minecraft.
# 
#    ----> This will probably require checks for the operating system +
#          OS-dependent shell commands.

# ---------------------------------------------------------------------------- # 
# Standard library
# ---------------------------------------------------------------------------- # 
import platform
import subprocess


if __name__ == '__main__':
    OS = platform.system()

    if OS == 'Windows':
        print('IMPLEMENTING...')
    else:
        print(f'This script does not support {OS} yet! Open an issue so we can add support...')
