from matplotlib.backends import wasm_backend
from js import document

class FigureCanvas240(wasm_backend.FigureCanvasWasm):
    def __init__(self, *args, **kwargs):
        wasm_backend.FigureCanvasWasm.__init__(self, *args, **kwargs)

    def create_root_element(self):
        try:
            parent = document.getElementById('imagediv')
            if parent.lastElementChild.tagName == 'DIV':
                parent.lastElementChild.innerHTML = ''
                return parent.lastElementChild
            else:
                newelement = document.createElement("div")
                parent.append(newelement)
                return newelement
        except Exception as e:
            print(e)
            return document.createElement("div")

wasm_backend.FigureCanvas.create_root_element = FigureCanvas240.create_root_element

wasm_backend.FigureCanvas = FigureCanvas240
