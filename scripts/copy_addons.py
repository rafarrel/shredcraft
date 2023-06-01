"""
    This script copies all changes to addon packs being developed to Minecraft's
    'com.mojang' folder automatically. This way, we don't have to copy all the
    files over manually every time we want to test changes.

    To run this script, execute from the top-level directory of the project:
    ```
        python scripts/copy_addons.py
    ```
"""
# ---------------------------------------------------------------------------- # 
# Standard library
# ---------------------------------------------------------------------------- # 
import pathlib
import shutil
from typing import Any


# Paths
HOME_DIR = pathlib.Path.home()
PROJECT_ROOT_DIR = pathlib.Path(__file__).parent.parent
PROJECT_SOURCE_DIR = PROJECT_ROOT_DIR.joinpath('src')
MINECRAFT_PACKS_DIR = HOME_DIR.joinpath('AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang')


if __name__ == '__main__':
    for pack_filepath in PROJECT_SOURCE_DIR.iterdir():
        pack_type = pack_filepath.name
        if pack_type in ('behavior', 'resource'):
            new_filepath = MINECRAFT_PACKS_DIR.joinpath(
                f'development_{pack_type}_packs/ShredCraft_dev_{pack_type}')
            shutil.rmtree(path=new_filepath, ignore_errors=True)
            shutil.copytree(
                src=pack_filepath, 
                dst=new_filepath, 
                dirs_exist_ok=True)
