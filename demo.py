from taipy.gui import Gui
from taipy_konva import Library as KonvaLibrary
from taipy_konva import Layer, Text, Rect

layer = Layer()
layer.add(Text("some text", fill="yellow"))
layer.add(Rect(x=20, y=20, width=50, height=50, fill="red"))

layers = [layer]

page = """
# Konva demo

<|{layers}|konva.stage|>
"""
gui = Gui(page=page)
gui.add_library(KonvaLibrary())
if __name__ == "__main__":
    # Run main app
    gui.run(run_browser=False)
