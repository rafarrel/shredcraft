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
    for pack in PROJECT_SOURCE_DIR.iterdir():
        pack_name = pack.name
        if pack_name in ('behavior', 'resource'):
            dev_packs_dir = MINECRAFT_PACKS_DIR.joinpath(f'development_{pack_name}_packs')
            new_pack_dir = dev_packs_dir.joinpath(f'ShredCraft_dev_{pack_name}')
            shutil.copytree(src=pack, dst=new_pack_dir)
