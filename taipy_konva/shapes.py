import typing as t
from abc import ABC


class Shape(ABC):
    def __init__(self, **kwargs):
        self.args = kwargs

    def _to_json(self):
        def to_json(v) -> str:
            if isinstance(v, bool):
                return str(v).lower()
            elif isinstance(v, (int, float)):
                return str(v)
            else:
                return f'"{str(v)}"'

        props = ",".join(f'"{k}":{to_json(v)}' for k, v in self.args.items())
        return f'"type":"{type(self).__name__}","p":{{{props}}}'


class Rect(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Text(Shape):
    def __init__(self, text: t.Optional[str], **kwargs):
        if text:
            kwargs["text"] = text
        super().__init__(**kwargs)
