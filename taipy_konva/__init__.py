# Export the library class for easier access by developers using it
from .library import Library  # noqa: F401
from .layer import Layer  # noqa: F401
from .shapes import Text, Rect  # noqa: F401
from taipy.gui import JsonAdapter as TaipyGuiJsonAdapter
import typing as t


class JsonAdapter(TaipyGuiJsonAdapter):
    def parse(self, o) -> t.Optional[t.Any]:
        if isinstance(o, Layer):
            return o._to_json()

JsonAdapter().register()

