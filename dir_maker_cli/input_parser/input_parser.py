from abc import ABC, abstractmethod
from dir_maker_cli.models.command import Command


class InputParser(ABC):
    @abstractmethod
    def parse(self) -> Command | None:
        raise NotImplementedError("parse() must be implemented")

    @abstractmethod
    def help(self) -> str:
        raise NotImplementedError("help() must be implemented")
