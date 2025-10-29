# entidades/nutricion.py

class Comida:
    """
    Entidad que representa una sugerencia de comida.
    """
    def __init__(self, nombre: str, descripcion: str, calorias: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.calorias = calorias

    def get_nombre(self) -> str:
        return self.nombre
