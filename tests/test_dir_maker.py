from dir_maker_cli.dir_maker import create_directories
from dir_maker_cli.models.command import Command
import os
import shutil


def test_directory_creation(tmp_path):
    """Test creation of different directory series in temp folder"""

    # tmp_path is a pytest fixture which will create a temp directory for test purposes
    target_path = tmp_path

    # Test creation based on range_to parameter
    # range_to is inclusive so that the loop must go one step further
    create_directories(target_path, Command(10))
    for i in range(1, 11):
        dir_path = os.path.join(target_path, f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        # remove the directories so that tests below face an empty path
        shutil.rmtree(dir_path)

    # Test creation based on range_from, range_to parameters
    create_directories(target_path, Command(range_from=2, range_to=15))
    for i in range(2, 16):
        dir_path = os.path.join(target_path, f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        # remove the directories so that tests below face an empty path
        shutil.rmtree(dir_path)

    # Test creation based on range_from, range_to and container_dir parameters
    create_directories(
        target_path, Command(range_from=10, range_to=20, container_dir="temp_container")
    )
    for i in range(10, 21):
        dir_path = os.path.join(target_path, "temp_container", f"{i}")
        assert os.path.isdir(dir_path), f"Directory does not exist {dir_path}"
        # remove the directories so that tests below face an empty path
        shutil.rmtree(dir_path)
