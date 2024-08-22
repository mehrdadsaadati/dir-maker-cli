from dir_maker_cli.models.command import Command
import os


def create_directories(target_path: str, command: Command):
    base_path = (
        target_path
        if command.container_dir is None
        else os.path.join(target_path, command.container_dir)
    )
    for i in range(command.range_from, command.range_to + 1):
        dir_path = os.path.join(base_path, f"{i}")
        os.makedirs(dir_path, exist_ok=True)
