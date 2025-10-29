# servicios/servicio_perfil.py
import pickle
import os
from typing import Optional

from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.excepciones.kickboxing_exception import PersistenciaException

DATA_DIR = "data"

class ServicioPerfil:
    """Servicio para gestionar la persistencia del perfil del atleta."""

    def persistir(self, perfil: PerfilDeLuchador) -> None:
        """
        Guarda el perfil del atleta en un archivo .dat usando pickle.

        Args:
            perfil: La instancia de PerfilDeLuchador a guardar.

        Raises:
            PersistenciaException: Si ocurre un error durante la escritura del archivo.
        """
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        file_path = os.path.join(DATA_DIR, f"{perfil.get_nombre()}.dat")
        try:
            with open(file_path, "wb") as f:
                pickle.dump(perfil, f)
        except (IOError, pickle.PicklingError) as e:
            raise PersistenciaException(f"Error al guardar el perfil: {e}") from e

    def recuperar(self, nombre_atleta: str) -> Optional[PerfilDeLuchador]:
        """
        Carga un perfil de atleta desde un archivo .dat.

        Args:
            nombre_atleta: El nombre del atleta para encontrar el archivo.

        Returns:
            La instancia de PerfilDeLuchador si se encuentra, de lo contrario None.

        Raises:
            PersistenciaException: Si ocurre un error durante la lectura del archivo.
        """
        file_path = os.path.join(DATA_DIR, f"{nombre_atleta}.dat")
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, "rb") as f:
                return pickle.load(f)
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(f"Error al recuperar el perfil: {e}") from e
