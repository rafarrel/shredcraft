# ---------------------------------------------------------------------------- # 
# Standard library
# ---------------------------------------------------------------------------- # 
import pathlib
import shutil


if __name__ == '__main__':
    HOME_DIR = pathlib.Path.home()
    PROJECT_ROOT_DIR = pathlib.Path(__file__).parent.parent
    PROJECT_SOURCE_DIR = PROJECT_ROOT_DIR.joinpath('src')
    MINECRAFT_PACKS_DIR = HOME_DIR.joinpath('AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang')

    # Copy addon packs to the development folders in 'com.mojang'
    for pack_filepath in PROJECT_SOURCE_DIR.iterdir():
        pack_type = pack_filepath.name
        if pack_type in ('behavior', 'resource'):
            new_filepath = MINECRAFT_PACKS_DIR.joinpath(
                f'development_{pack_type}_packs/ShredCraft_dev_{pack_type}')
            shutil.copytree(
                src=pack_filepath, 
                dst=new_filepath, 
                dirs_exist_ok=True)
