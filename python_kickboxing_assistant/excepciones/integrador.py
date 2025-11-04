"""
Archivo integrador generado automaticamente
Directorio: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/excepciones
Fecha: 2025-11-04 16:21:12
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: kickboxing_exception.py
# Ruta: /home/martinsalvatore/repos/python/asistente_kickboxing/python_kickboxing_assistant/excepciones/kickboxing_exception.py
# ================================================================================

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


