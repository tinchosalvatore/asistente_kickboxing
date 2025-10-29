# entidades/perfil_atleta.py
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .sesion_entrenamiento import SesionDeEntrenamiento

class PerfilDeLuchador:
    """
    Entidad que representa el perfil de un atleta.
    Contiene datos demográficos, de salud y el historial de entrenamiento.
    Esta clase solo contiene datos, la lógica de negocio está en los servicios.
    """
    def __init__(self, nombre: str, peso: float, altura: float):
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")

        self.nombre: str = nombre
        self.peso: float = peso
        self.altura: float = altura
        self.estado_salud: str = "Óptimo"
        self.sesiones: List['SesionDeEntrenamiento'] = []

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_peso(self, peso: float):
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        self.peso = peso

    def set_altura(self, altura: float):
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.altura = altura

    def get_nombre(self) -> str:
        return self.nombre

    def get_estado_salud(self) -> str:
        return self.estado_salud

    def set_estado_salud(self, estado: str):
        self.estado_salud = estado

    def agregar_sesion(self, sesion: 'SesionDeEntrenamiento'):
        self.sesiones.append(sesion)
