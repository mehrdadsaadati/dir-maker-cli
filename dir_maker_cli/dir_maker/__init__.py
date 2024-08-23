from dir_maker_cli.models.command import Command
import os


def create_directories(target_path: str, command: Command):
    """Creates a list of directories based on the input command.

    Parameters
    ----------
    target_path: str
        name of the target base directory. If command has container_dir, final path will be the join of target_path and container_dir
    command: Command
        the user command indicating the sequence number range and container_dir name
    """

    # create path based on the container_dir.
    # target_path is the base directory to create directories inside. If container_dir is passed, we should join it to the target_path
    base_path = (
        target_path
        if command.container_dir is None
        else os.path.join(target_path, command.container_dir)
    )
    # iterate from range_from to range_to
    # range_to is inclusive so we iterate one step further in for loop to cover it
    for i in range(command.range_from, command.range_to + 1):
        dir_path = os.path.join(base_path, f"{i}")
        # create directories, ignoring if it exists there beforehand
        os.makedirs(dir_path, exist_ok=True)
