import tarfile

imagenette_tar_path = "./imagenette2-160.tgz"

with tarfile.open(imagenette_tar_path, "r") as tar:
    tar.extractall("./")

import os
os.makedirs("./working_dataset")
os.makedirs("./working_dataset/all")

os.makedirs("./working_dataset/all/parachute")
os.makedirs("./working_dataset/all/gas pump")
os.makedirs("./working_dataset/all/french horn")
os.makedirs("./working_dataset/all/garbage truck")
os.makedirs("./working_dataset/all/english springer")

import shutil

source_dir = './imagenette2-160/val/n03888257'
destination_dir = './working_dataset/all/parachute'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/train/n03888257'
destination_dir = './working_dataset/all/parachute'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/val/n03417042/'
destination_dir = './working_dataset/all/garbage truck'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/train/n03417042/'
destination_dir = './working_dataset/all/garbage truck'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/val/n03394916/'
destination_dir = './working_dataset/all/french horn'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/train/n03394916/'
destination_dir = './working_dataset/all/french horn'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/val/n03425413/'
destination_dir = './working_dataset/all/gas pump'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/train/n03425413/'
destination_dir = './working_dataset/all/gas pump'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/val/n02102040/'
destination_dir = './working_dataset/all/english springer'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

source_dir = './imagenette2-160/train/n02102040/'
destination_dir = './working_dataset/all/english springer'

shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

import splitfolders

splitfolders.ratio("./working_dataset/all/", output="./working_dataset/split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)
