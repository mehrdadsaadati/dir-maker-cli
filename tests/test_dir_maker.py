from dir_maker_cli.dir_maker.dir_maker import create_directories
from dir_maker_cli.models.command import Command
import os
import shutil


def test_directory_creation(tmp_path):
    target_path = tmp_path
    create_directories(target_path, Command(10))
    for i in range(1, 11):
        dir_path = os.path.join(target_path, f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        shutil.rmtree(dir_path)

    create_directories(target_path, Command(range_from=2, range_to=15))
    for i in range(2, 16):
        dir_path = os.path.join(target_path, f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        shutil.rmtree(dir_path)

    create_directories(
        target_path, Command(range_from=10, range_to=20, container_dir="temp_container")
    )
    for i in range(10, 21):
        dir_path = os.path.join(target_path, "temp_container", f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        shutil.rmtree(dir_path)
