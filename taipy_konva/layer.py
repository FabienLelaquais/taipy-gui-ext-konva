from .shapes import Shape


class Layer():
    def __init__(self):
        self.shapes = []
    
    def add(self, shape: Shape) -> None:
        self.shapes.append(shape)


    def _to_json(self) -> str:
        shapes = ",".join(f"{{{shape._to_json()}}}" for shape in self.shapes)
        return f'{{"shapes":[{shapes}]}}'
