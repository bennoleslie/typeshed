from typing import Any, Optional

__revision__ = ...  # type: str

def isInt(x): ...

class AllOrNothing:
    def __init__(self, ciphermodule, mode: Optional[Any] = ..., IV: Optional[Any] = ...) -> None: ...
    def digest(self, text): ...
    def undigest(self, blocks): ...
