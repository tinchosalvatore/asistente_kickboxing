"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: movimiento.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/movimiento.py
# ================================================================================

# entidades/movimiento.py
from abc import ABC, abstractmethod

class Movimiento(ABC):
    """
    Interfaz que representa un movimiento de kickboxing.
    """
    def __init__(self, nombre: str, potencia: int, calorias: float):
        self._nombre = nombre
        self._potencia = potencia
        self._calorias = calorias

    def get_nombre(self) -> str:
        return self._nombre

    def get_potencia(self) -> int:
        return self._potencia

    def get_calorias(self) -> float:
        return self._calorias

    @abstractmethod
    def es_combinacion(self) -> bool:
        """Devuelve True si el movimiento es una combinación de otros."""
        pass


# ================================================================================
# ARCHIVO 3/5: nutricion.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/nutricion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/5: perfil_atleta.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/perfil_atleta.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: sesion_entrenamiento.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/entidades/sesion_entrenamiento.py
# ================================================================================

# entidades/sesion_entrenamiento.py
from __future__ import annotations
from typing import List, Dict, Any, Optional, TYPE_CHECKING
from .movimiento import Movimiento

from python_kickboxing_assistant.patrones.observer.observable import Observable

if TYPE_CHECKING:
    from .perfil_atleta import PerfilDeLuchador
    from ..patrones.strategy.evaluacion_strategy import EvaluacionStrategy

class SesionDeEntrenamiento(Observable['SesionDeEntrenamiento']):
    """
    Entidad que representa una sesión de entrenamiento.
    También es un Observable que notifica eventos de su ciclo de vida.
    """
    def __init__(self, tipo: str, atleta: 'PerfilDeLuchador', estrategia_evaluacion: 'EvaluacionStrategy'):
        super().__init__()
        self.tipo: str = tipo
        self.atleta: 'PerfilDeLuchador' = atleta
        self.estrategia_evaluacion: 'EvaluacionStrategy' = estrategia_evaluacion
        self.movimientos: List[Movimiento] = []
        self.resultado_evaluacion: Optional[Dict[str, Any]] = None

    def agregar_movimiento(self, movimiento: Movimiento):
        self.movimientos.append(movimiento)

    def get_movimientos(self) -> List[Movimiento]:
        return self.movimientos.copy() # Defensive copy

    def set_resultado_evaluacion(self, resultado: Dict[str, Any]):
        self.resultado_evaluacion = resultado

    def evaluar(self) -> None:
        """
        Evalúa la sesión utilizando la estrategia de evaluación asignada
        y almacena el resultado.
        """
        self.resultado_evaluacion = self.estrategia_evaluacion.evaluar(self)

    def get_resultado_evaluacion(self) -> Optional[Dict[str, Any]]:
        """
        Devuelve el resultado de la evaluación de la sesión.
        """
        return self.resultado_evaluacion

    def finalizar(self):
        """Notifica a los observadores que la sesión ha finalizado, pasando la sesión completa."""
        self.notificar_observadores(self)


