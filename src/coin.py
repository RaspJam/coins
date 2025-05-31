from typing import Union, Callable, Optional
from word2number import w2n

class CoinContext:
    input: Optional[str]
    number: Optional[Union[int, float]]
    string: Optional[str]

    def __init__(
        self, input: Optional[str], number: Optional[str], string: Optional[str]
    ) -> None:
        self.input = input
        self.number = w2n.word_to_num(number) if number is not None else None
        self.string = string


class CoinBank:
    data: dict[str, dict[str, Optional[Callable]]]
    last_command: Optional[str]

    def __init__(self) -> None:
        self.data = {}

    def add_command(self, command: str, default_func: Optional[Callable] = None):
        if command in self.data:
            if default_func == self.data["command"].get("default"):
                raise ValueError(f'Command "{command}" already exists!')

        self.data[command] = {"default": default_func}

    def add_option(self, command: Optional[str], option: str, func: Callable):
        # if command is None:
        #     if self.last_command is None:
        #         raise ValueError(f'Option "{option}" needs an explicit command name!')
        #     command = self.last_command  # Use last declared command if available

        if command not in self.data:
            raise ValueError(f'Command "{command}" does not exist in the CoinBank')

        if option in self.data[command]:
            raise ValueError(f'Pair "{command}:{option}" already exists')

        self.data[command][option] = func


BANK = CoinBank()