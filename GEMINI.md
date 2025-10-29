# Guía de Contexto para Gemini - Asistente de Entrenamiento de Kickboxing

**Proyecto**: Kickboxing Assistant
**Versión**: 1.0.0
**Python**: 3.13+
**Fecha**: Octubre 2025

---

## 🎯 Propósito del Proyecto

Sistema integral de gestión de entrenamiento de kickboxing que implementa **5 patrones de diseño principales** (Singleton, Factory Method, Observer, Strategy, Registry) con un enfoque educativo y práctico. El sistema gestiona perfiles de atletas, sesiones de entrenamiento, evaluación de rendimiento, salud, nutrición y persistencia de datos.

---

## 📋 Tabla de Contenidos

1. [Contexto General](#contexto-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Patrones de Diseño](#patrones-de-diseño)
4. [Convenciones de Código](#convenciones-de-código)
5. [Reglas Críticas](#reglas-críticas)
6. [Estructura de Archivos](#estructura-de-archivos)
7. [Flujos de Trabajo Comunes](#flujos-de-trabajo-comunes)
8. [Testing y Validación](#testing-y-validación)

---

## 🌍 Contexto General

### Dominio del Problema

El sistema gestiona el entrenamiento de un atleta de deportes de combate con:

- **Múltiples tipos de movimientos**: Jab, Cross, LowKick, etc.
- **Sistema de entrenamiento en tiempo real**: 2 threads daemon (Timer, Coach).
- **Gestión de la salud del atleta**: Análisis post-sparring y estado de salud.
- **Sugerencias de nutrición**: Recomendaciones de comida post-entrenamiento.
- **Persistencia**: Serialización del perfil del atleta con Pickle en `data/`.

### Entidades Principales

```
KickboxingServiceRegistry (raíz, Singleton)
  └── PerfilDeLuchador
        ├── SesionesDeEntrenamiento[]
        │     └── Movimientos[] (Jab, Cross, etc.)
        └── EstadoDeSalud
```

### Flujo de Operaciones Típico

```
1. Iniciar Sistema -> Se crea/carga el PerfilDeLuchador (Singleton).
2. Iniciar Sesión -> Se crea una SesionDeEntrenamiento con una Strategy de evaluación.
3. Iniciar Threads -> Se inician TimerTask y CoachTask (Observables).
4. Entrenamiento -> El Coach "canta" movimientos, el Factory los crea, se añaden a la sesión.
5. Finalizar Sesión -> Los Observers (AnalizadorDeSalud) reaccionan.
6. Evaluación -> La Strategy de la sesión calcula el rendimiento.
7. Nutrición -> Una Strategy de comida sugiere un plan de recuperación.
8. Persistir -> Se guarda el estado actualizado del PerfilDeLuchador.
```

---

## 🏗️ Arquitectura del Sistema

La arquitectura es en capas y sigue los principios SOLID, idéntica a la del proyecto de referencia.

- **SRP**: Entidades = datos, Servicios = lógica.
- **OCP**: Extensible vía Strategy y Factory.
- **LSP**: Todos los movimientos son `Movimiento`.
- **ISP**: Interfaces específicas (`Observer[T]`, `EvaluacionStrategy`).
- **DIP**: Servicios dependen de abstracciones.

---

## 🎨 Patrones de Diseño

### 1. SINGLETON

**Ubicación**: `python_kickboxing_assistant/servicios/kickboxing_service_registry.py`

**Propósito**: Instancia única del registro de servicios y del perfil del atleta, compartida por toda la aplicación.

**Implementación Crítica**:
```python
class KickboxingServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance
```

---

### 2. FACTORY METHOD

**Ubicación**: `python_kickboxing_assistant/patrones/factory/movimiento_factory.py`

**Propósito**: Creación centralizada de movimientos sin conocer las clases concretas.

**Implementación Crítica**:
```python
class MovimientoFactory:
    _constructores = {
        "Jab": Jab,
        "Cross": Cross,
        "LowKick": LowKick
    }

    @staticmethod
    def crear_movimiento(tipo: str) -> Movimiento:
        constructor = MovimientoFactory._constructores.get(tipo)
        if not constructor:
            raise ValueError(f"Movimiento desconocido: {tipo}")
        return constructor()
```
**REGLA**: Cliente NUNCA instancia movimientos directamente. SIEMPRE usar factory.

---

### 3. OBSERVER

**Ubicación**: `python_kickboxing_assistant/patrones/observer/`

**Propósito**: Notificación automática entre los componentes de tiempo real (Timer, Coach) y los controladores o analizadores.

**Implementación Crítica**:
```python
# Observable: El Timer del Round
class TimerTask(threading.Thread, Observable[str]):
    def run(self):
        while not self._detenido.is_set():
            self.notificar_observadores("INICIO_ROUND")
            time.sleep(self._duracion_round)
            self.notificar_observadores("FIN_ROUND")

# Observer: Un controlador que reacciona
class ControladorDeSesion(Observer[str]):
    def actualizar(self, evento: str) -> None:
        if evento == "INICIO_ROUND":
            print("¡A PELEAR!")
```

---

### 4. STRATEGY

**Ubicación**: `python_kickboxing_assistant/patrones/strategy/`

**Propósito**: Algoritmos intercambiables para evaluar sesiones, sugerir comidas, etc.

**Implementación Crítica**:
```python
# Interfaz
class EvaluacionStrategy(ABC):
    @abstractmethod
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> dict:
        pass

# Estrategia Concreta 1
class EstrategiaDeCalorias(EvaluacionStrategy):
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> dict:
        total = sum(m.get_calorias() for m in sesion.get_movimientos())
        return {"tipo": "Calorías", "valor": total}

# Inyección en el servicio
servicio_ent = ServicioEntrenamiento()
sesion = servicio_ent.iniciar_sesion(
    ...,
    estrategia_evaluacion=EstrategiaDeCalorias()
)
```

---

### 5. REGISTRY

**Ubicación**: Integrado en `KickboxingServiceRegistry`.

**Propósito**: Eliminar cascadas de `isinstance()` con dispatch polimórfico.

**Implementación Crítica**:
```python
class KickboxingServiceRegistry:
    def _inicializar(self):
        self._manejadores_display = {
            Jab: self._display_jab,
            Cross: self._display_cross
        }

    def mostrar_movimiento(self, movimiento: Movimiento):
        manejador = self._manejadores_display.get(type(movimiento))
        if manejador: manejador(movimiento)
```

---

## 📝 Convenciones de Código

Idénticas al proyecto original: PEP 8, Type Hints, Docstrings de Google, estructura de imports.

---

## ⚠️ Reglas Críticas

### 🚫 PROHIBIDO
1.  **Magic Numbers**: Usar `constantes.py` para `POTENCIA_JAB`, `DURACION_ROUND`, etc.
2.  **Lambdas**: Usar métodos estáticos o de instancia nombrados.
3.  **Instanciación Directa de Movimientos**: Siempre usar `MovimientoFactory`.
4.  **`isinstance()` Cascades**: Usar el patrón `Registry` para dispatch.
5.  **Lógica de Negocio en Entidades**: Las entidades (`Movimiento`, `PerfilDeLuchador`) solo contienen datos.

### ✅ OBLIGATORIO
1.  Todas las constantes en `constantes.py`.
2.  Type hints en todas las firmas públicas.
3.  Docstrings en clases y métodos públicos.
4.  Defensive copying para listas.
5.  Validación en setters (ej. `set_peso` no puede ser negativo).

---

## 📁 Estructura de Archivos

(La estructura detallada se encuentra en `README_kick.md`)

---

## 🔄 Flujos de Trabajo Comunes

### Agregar Nuevo Movimiento (Ej: "UpperCut")

1.  **`constantes.py`**: Añadir `POTENCIA_UPPERCUT`, `CALORIAS_UPPERCUT`.
2.  **Crear entidad** (`entidades/movimientos/uppercut.py`): `class UpperCut(Movimiento): ...`
3.  **Crear servicio** (si necesita lógica especial) o usar el base.
4.  **Registrar en Registry** (`kickboxing_service_registry.py`): Añadir un handler en `_manejadores_display` para `UpperCut`.
5.  **Registrar en Factory** (`movimiento_factory.py`): Añadir `"UpperCut": UpperCut` al diccionario `_constructores`.
6.  **Usar**: `MovimientoFactory.crear_movimiento("UpperCut")`.

### Agregar Nueva Estrategia de Evaluación

1.  **Crear estrategia** (`patrones/strategy/impl/estrategia_de_resistencia.py`): `class EstrategiaDeResistencia(EvaluacionStrategy): ...`
2.  **Inyectar en servicio**: `servicio_ent.iniciar_sesion(..., estrategia_evaluacion=EstrategiaDeResistencia())`.

---

## 🧪 Testing y Validación

### Ejecutar Sistema Completo

```bash
python main_kickboxing.py
```

**Salida esperada**: Ver `README_kick.md` sección "Instalación". El sistema debe ejecutar una sesión de demostración y persistir el perfil.

### Casos de Prueba Críticos

1.  **Atleta no apto**: Si el `estado_salud` del perfil es `"Descanso Obligatorio"`, intentar iniciar una sesión de sparring debe lanzar `AtletaNoAptoException`.
2.  **Movimiento desconocido**: `MovimientoFactory.crear_movimiento("PatadaImaginaria")` debe lanzar `ValueError`.
3.  **Persistencia**: Verificar que el archivo `{nombre_atleta}.dat` se crea/actualiza en la carpeta `data/`.

---

## 💡 Consejos para Gemini

-   **Prioridad a los Planos**: Siempre referenciar `README_kick.md` y `USER_STORIES_kick.md` antes de escribir código.
-   **Foco en los Patrones**: La correcta implementación de los 5 patrones es el objetivo principal.
-   **Separación Estricta**: Mantener la disciplina de no poner lógica en entidades.
-   **Constantes Centralizadas**: No hardcodear ningún valor numérico o string literal que pueda ser una constante.

**¡Listo para construir el Asistente de Kickboxing! 🥊**
