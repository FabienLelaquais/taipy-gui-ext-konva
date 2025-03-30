from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType


class Library(ElementLibrary):

    def get_name(self) -> str:
        return "konva"

    def get_elements(self) -> dict:
        return {
            # Declare the elements of the library here, as key/value pairs of
            # a dictionary.
            # - The key is used as the element name.
            # - The value must be an instance of taipy.gui.extension.Element
            "stage": Element(
                "layers",
                {
                    "layers": ElementProperty(PropertyType.dynamic_any),
                },
                react_component="Stage",
            )
        }

    def get_scripts(self) -> list[str]:
        return ["front-end/dist/taipy-konva.js"]
