class Command:
    def __init__(
        self, range_to: int, range_from: int = 0, container_dir: str = None
    ) -> None:
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
