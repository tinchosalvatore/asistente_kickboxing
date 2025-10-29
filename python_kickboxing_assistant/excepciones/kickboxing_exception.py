# excepciones/kickboxing_exception.py

class KickboxingException(Exception):
    """Clase base para todas las excepciones personalizadas del sistema."""
    pass

class PersistenciaException(KickboxingException):
    """Lanzada cuando ocurre un error durante la serialización o deserialización del perfil."""
    pass

class AtletaNoAptoException(KickboxingException):
    """Lanzada cuando un atleta intenta entrenar pero su estado de salud no es 'Óptimo'."""
    pass
