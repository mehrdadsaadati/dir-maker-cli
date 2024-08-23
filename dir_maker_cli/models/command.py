class Command:
    """A DTO to pass user requests to different parts of the app

    Attributes
    ----------
        range_from: int
            Starting number to create directories
        range_to: int
            Last number (inclusive) to create directories
        container_dir: str
            Name of the parent directory to create directories inside

    """

    def __init__(
        self, range_to: int, range_from: int = 1, container_dir: str = None
    ) -> None:
        """
        Parameters
        ----------
            range_from: int, optional
                Starting number to create directories (default 1)
            range_to: int
                Last number (inclusive) to create directories
            container_dir: str, optional
                Name of the parent directory to create directories inside. If not passed, the current directory will be used.

        """

        self.range_from = range_from
        self.range_to = range_to
        self.container_dir = container_dir

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Command):
            return (
                self.range_from == value.range_from
                and self.range_to == value.range_to
                and self.container_dir == value.container_dir
            )
        else:
            return False
