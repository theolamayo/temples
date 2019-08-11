from pathlib import Path

from .config import get_absolute_path


class Data(object):
    def __init__(self, path: str, relative_to_config: bool = False) -> None:
        if relative_to_config:
            path = get_absolute_path(path)
        self.path = Path(path)
        self._data = None

    def load(self) -> None:
        return None

    def write(self) -> None:
        raise NotImplementedError

    def exists(self) -> bool:
        return self.path.exists()
