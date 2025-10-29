# Asistente de Entrenamiento de Kickboxing: Especificación Técnica Completa

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema de gestión de entrenamiento de kickboxing que demuestra la implementación de múltiples patrones de diseño de software con un enfoque práctico, modular y educativo.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#características-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseño-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Módulos del Sistema](#módulos-del-sistema)
- [Documentación Técnica](#documentación-técnica)
- [Testing y Validación](#testing-y-validación)
- [Contribución](#contribución)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El **Asistente de Entrenamiento de Kickboxing** aborda los desafíos de un entrenamiento estructurado y medible para atletas de deportes de combate, un dominio que requiere:

1.  **Gestión de Múltiples Tipos de Actividades**:
    *   Diferenciación entre golpes, patadas, defensas y combinaciones complejas.
    *   Registro de actividades específicas como sparring, saco pesado o sombra.
    *   Cada movimiento con características y métricas de evaluación únicas.

2.  **Monitoreo del Atleta en Tiempo Real**:
    *   Control de tiempo por rounds y descansos mediante hilos de ejecución.
    *   Un "Coach Virtual" que propone combinaciones y guía el entrenamiento.
    *   Respuesta dinámica a la intensidad del ejercicio (ej. ritmo cardíaco).

3.  **Análisis de Salud y Recuperación**:
    *   Evaluación del estado del atleta después de sesiones de alto impacto como el sparring.
    *   Recomendaciones de descanso basadas en la intensidad del entrenamiento.
    *   Sugerencias de comidas post-entrenamiento para optimizar la recuperación.

4.  **Planificación de Sesiones y Objetivos**:
    *   Definición de objetivos por sesión (quema de calorías, mejora de técnica, resistencia).
    *   Adaptación del entrenamiento según las metas del atleta.

5.  **Persistencia y Seguimiento del Progreso**:
    *   Almacenamiento del perfil del atleta, incluyendo récords personales (ej. golpe más fuerte, combo más rápido).
    *   Recuperación de historiales de entrenamiento para analizar la evolución.

### Actores del Sistema

-   **Atleta/Usuario**: Utiliza el sistema para guiar y registrar sus entrenamientos.
-   **Coach Virtual**: Componente automatizado que dicta el ritmo y los ejercicios de la sesión.
-   **Analizador de Salud**: Evalúa el estado del atleta y emite recomendaciones.
-   **Sensores (Teóricos)**: Monitores de ritmo cardíaco o impacto que proporcionan datos en tiempo real.

### Flujo de Operaciones Típico

```
1. CREACIÓN PERFIL --> Se crea el PerfilDeLuchador único (Singleton).
2. INICIO SESIÓN --> El atleta elige un tipo de entrenamiento (ej. "Saco Pesado").
3. EJECUCIÓN --> El Timer (Observer) inicia el round. El Coach Virtual (Observer) "canta" combinaciones. El Factory crea los movimientos correspondientes.
4. EVALUACIÓN --> Una Strategy calcula las métricas de la sesión (calorías, puntuación).
5. FIN SESIÓN --> El Timer notifica el final. Se activa el análisis post-entrenamiento.
6. ANÁLISIS SALUD --> Si fue sparring, un Analizador (Observer) evalúa la condición y da recomendaciones (usando una Strategy).
7. SUGERENCIA COMIDA --> El sistema elige una ComidaStrategy y recomienda un plan de recuperación nutricional.
8. PERSISTENCIA --> El PerfilDeLuchador se actualiza y guarda con los nuevos datos.
```

---

## Características Principales

### Funcionalidades del Sistema

#### 1. Gestión de Movimientos y Combinaciones
- **Creación dinámica** de movimientos de combate vía **Factory Pattern**:
  - **Golpes**: Jab, Cross, Hook, Uppercut.
  - **Patadas**: Low Kick, Middle Kick, High Kick, Front Kick.
  - **Defensas**: Bloqueo, Esquiva.
  - **Combinaciones**: Secuencias predefinidas de movimientos (ej: "Jab-Cross-LowKick").
- **Catálogo extensible** para añadir nuevos movimientos sin modificar el código cliente.

#### 2. Entrenamiento Interactivo y en Tiempo Real
- **Guía por rounds** con temporizador concurrente (hilo) basado en el **patrón Observer**.
- **"Coach Virtual"** que propone combinaciones en tiempo real, actuando como un **Observable**.
- **Evaluación basada en objetivos** mediante el **patrón Strategy**:
  - `EstrategiaDeCalorias`: Maximiza el gasto energético.
  - `EstrategiaDePuntuacion`: Puntúa la ejecución de combos (simulado).
  - `EstrategiaDeResistencia`: Mantiene al atleta en una zona de ritmo cardíaco específica.

#### 3. Gestión Integral de la Salud del Atleta
- **Análisis post-sparring** automático (vía **Observer**) con recomendaciones de descanso (vía **Strategy**).
- **Sugerencias de comidas** adaptadas a la intensidad y tipo de entrenamiento (vía **Strategy**).
  - `EstrategiaComidaRecuperacion` para sesiones de fuerza.
  - `EstrategiaComidaLigera` para sesiones de técnica.
- **Estado de salud** del atleta ("Óptimo", "En Recuperación", "Descanso Obligatorio") gestionado centralmente.

#### 4. Perfil del Atleta y Persistencia
- **PerfilDeLuchador** implementado como un **Singleton** para garantizar un único punto de verdad.
- Almacena datos demográficos (peso, altura) y de rendimiento (récords, nivel, historial de sesiones).
- **Serialización con Pickle** del objeto `PerfilDeLuchador` para guardar el estado entre sesiones.
- Nombre de archivo dinámico: `{nombre_atleta}.dat`.

---

## Arquitectura del Sistema

### Principios Arquitectónicos

El sistema está diseñado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una única razón para cambiar (Entidades para datos, Servicios para lógica).
- **Open/Closed**: Abierto a extensión (nuevos movimientos, nuevas estrategias), cerrado a modificación.
- **Liskov Substitution**: Todos los movimientos son un `Movimiento`, todas las estrategias de evaluación son una `EvaluacionStrategy`.
- **Interface Segregation**: Interfaces específicas como `Observer[T]` y `EvaluacionStrategy`.
- **Dependency Inversion**: Los servicios dependen de abstracciones (interfaces de Strategy), no de implementaciones concretas.

### Separación de Capas

```
+----------------------------------+
|        PRESENTACIÓN              |
| (main_kickboxing.py - CLI Demo)  |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
| (ServicioEntrenamiento, etc.)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
| (ServicioEvaluacion, Salud)      |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
| (Movimiento, Sesion, Perfil)     |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
| (Factory, Strategy, Observer)    |
+----------------------------------+
```

### Inyección de Dependencias

El sistema utiliza inyección manual de dependencias para desacoplar componentes:

```python
# La estrategia de evaluación se inyecta en el servicio
servicio_eval = ServicioDeEvaluacion(EstrategiaDeCalorias())

# El AnalizadorDeSalud (Observer) se suscribe a la sesión (Observable)
sesion_sparring = ...
analizador_salud = AnalizadorDeSalud()
sesion_sparring.agregar_observador(analizador_salud)
```

---

## Patrones de Diseño Implementados

### 1. SINGLETON Pattern

**Ubicación**: `python_kickboxing_assistant/servicios/perfil/perfil_atleta.py`

**Problema que resuelve**: Garantizar que exista una única instancia del perfil del atleta, accesible globalmente para registrar progreso y consultar estadísticas de forma consistente.

**Implementación**:
```python
from threading import Lock

class PerfilDeLuchador:
    _instance = None
    _lock = Lock()

    def __new__(cls, nombre: str):
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_perfil(nombre)
        return cls._instance
```

### 2. FACTORY METHOD Pattern

**Ubicación**: `python_kickboxing_assistant/patrones/factory/movimiento_factory.py`

**Problema que resuelve**: Centralizar la creación de diferentes tipos de movimientos (Jab, Cross, etc.) sin exponer la lógica de instanciación al cliente. Facilita añadir nuevos movimientos.

**Implementación**:
```python
class MovimientoFactory:
    @staticmethod
    def crear_movimiento(tipo: str) -> Movimiento:
        if tipo == "Jab":
            return Jab(potencia=10, calorias=1)
        elif tipo == "Cross":
            return Cross(potencia=20, calorias=2)
        elif tipo == "LowKick":
            return LowKick(potencia=30, calorias=5)
        # ... más movimientos
        else:
            raise ValueError(f"Movimiento desconocido: {tipo}")
```

### 3. OBSERVER Pattern

**Ubicación**: `python_kickboxing_assistant/patrones/observer/`

**Problema que resuelve**: Desacoplar el `Timer` y el `CoachVirtual` de los componentes que necesitan reaccionar a sus eventos, como la interfaz de usuario o los analizadores.

**Implementación**:
```python
# El Timer del Round es un Observable que notifica eventos de tiempo
class TimerDelRound(threading.Thread, Observable[str]):
    def run(self):
        # ... lógica del tiempo ...
        self.notificar_observadores("INICIO_ROUND")
        # ...
        self.notificar_observadores("FIN_ROUND")

# La Interfaz (o un controlador) es un Observer
class ControladorDeSesion(Observer[str]):
    def actualizar(self, evento: str) -> None:
        if evento == "INICIO_ROUND":
            print("¡A PELEAR!")
        elif evento == "FIN_ROUND":
            print("¡DESCANSO!")
```

### 4. STRATEGY Pattern

**Ubicación**: `python_kickboxing_assistant/patrones/strategy/`

**Problema que resuelve**: Permitir que los algoritmos para evaluar una sesión, sugerir comidas o dar recomendaciones de salud sean intercambiables.

**Implementación**:
```python
class EvaluacionStrategy(ABC):
    @abstractmethod
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> float:
        pass

class EstrategiaDeCalorias(EvaluacionStrategy):
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> float:
        total_calorias = sum(mov.get_calorias() for mov in sesion.get_movimientos())
        return total_calorias

class EstrategiaDePuntuacion(EvaluacionStrategy):
    def evaluar(self, sesion: 'SesionDeEntrenamiento') -> float:
        total_puntos = sum(mov.get_potencia() for mov in sesion.get_movimientos())
        return total_puntos
```

### 5. REGISTRY Pattern (Bonus)

**Ubicación**: Integrado en `KickboxingServiceRegistry`.

**Problema que resuelve**: Eliminar cadenas de `if/elif isinstance()` al realizar operaciones sobre diferentes tipos de `Movimiento`, usando dispatch polimórfico.

**Implementación**:
```python
class KickboxingServiceRegistry:
    # ... (código del Singleton)
    def _inicializar_servicios_y_perfil(self):
        # ...
        self._manejadores_display = {
            Jab: self._display_jab,
            Cross: self._display_cross,
            LowKick: self._display_low_kick
        }

    def mostrar_movimiento(self, movimiento: Movimiento):
        manejador = self._manejadores_display.get(type(movimiento))
        if manejador:
            manejador(movimiento)
        else:
            print(f"Movimiento genérico: {movimiento.get_nombre()}")

    def _display_jab(self, mov: Jab):
        print(f"-> Jab rápido! Potencia: {mov.get_potencia()}")
    
    def _display_cross(self, mov: Cross):
        print(f"--> Cross potente! Potencia: {mov.get_potencia()}")

    def _display_low_kick(self, mov: LowKick):
        print(f"==> Low Kick demoledor! Potencia: {mov.get_potencia()}")
```

**Antes (con `isinstance`)**:
```python
if isinstance(mov, Jab):
    print(f"-> Jab rápido! Potencia: {mov.get_potencia()}")
elif isinstance(mov, Cross):
    print(f"--> Cross potente! Potencia: {mov.get_potencia()}")
# ... etc.
```

**Después (con Registry)**:
```python
registry = KickboxingServiceRegistry.get_instance()
registry.mostrar_movimiento(mov) # Despacho automático
```

---

## Requisitos del Sistema

- **Python 3.13** o superior.
- **Sistema Operativo**: Windows, Linux, macOS.
- **Dependencias**: Ninguna, solo la biblioteca estándar de Python.

---

## Instalación

1.  **Clonar Repositorio**: `git clone <url_del_repositorio>`
2.  **Crear Entorno Virtual**: `python -m venv .venv` y activarlo (`source .venv/bin/activate` en Linux/macOS).
3.  **Ejecutar**: `python main_kickboxing.py`

---

## Uso del Sistema

### Ejemplo de Código

```python
# main_kickboxing.py

# 1. Crear perfil del atleta (Singleton)
perfil = PerfilDeLuchador.get_instance("Rocky Balboa")

# 2. Iniciar servicio de entrenamiento
servicio_entrenamiento = ServicioDeEntrenamiento()

# 3. Crear una sesión de Saco Pesado con estrategia de calorías
sesion = servicio_entrenamiento.iniciar_sesion(
    tipo="Saco Pesado",
    atleta=perfil,
    estrategia_evaluacion=EstrategiaDeCalorias()
)

# 4. Iniciar el entrenamiento en vivo (Observer)
# Esto iniciaría los hilos del Timer y el Coach Virtual
# que "cantan" movimientos. El Factory los crea internamente.
servicio_entrenamiento.ejecutar_sesion_en_vivo(sesion, duracion_segundos=180)

# 5. Finalizar y evaluar
servicio_entrenamiento.finalizar_sesion(sesion)
resultado_evaluacion = sesion.get_resultado_evaluacion()
print(f"Total de calorías quemadas: {resultado_evaluacion}")

# 6. Obtener sugerencia de comida (Strategy)
sugerencia = servicio_entrenamiento.obtener_sugerencia_comida(sesion)
print(f"Comida recomendada: {sugerencia.get_nombre()}")

# 7. Persistir el progreso
servicio_perfil = ServicioPerfil()
servicio_perfil.persistir(perfil)
```

---

## Estructura del Proyecto

```
parcial_disenoSistemas/
|
+-- python_forestacion/            # Proyecto original
|
+-- python_kickboxing_assistant/   # NUEVO PROYECTO
|   +-- __init__.py
|   +-- constantes.py
|   |
|   +-- entidades/
|   |   +-- __init__.py
|   |   +-- movimiento.py          # Interfaz base
|   |   +-- sesion_entrenamiento.py
|   |   +-- perfil_atleta.py
|   |   +-- nutricion.py
|   |
|   +-- servicios/
|   |   +-- __init__.py
|   |   +-- servicio_entrenamiento.py
|   |   +-- servicio_evaluacion.py
|   |   +-- servicio_salud.py
|   |   +-- servicio_perfil.py
|   |   +-- perfil_service_registry.py # Singleton + Registry
|   |
|   +-- patrones/
|   |   +-- __init__.py
|   |   +-- factory/
|   |   |   +-- movimiento_factory.py
|   |   +-- observer/
|   |   |   +-- observable.py
|   |   |   +-- observer.py
|   |   +-- strategy/
|   |       +-- __init__.py
|   |       +-- evaluacion_strategy.py
|   |       +-- comida_strategy.py
|   |       +-- salud_strategy.py
|   |       +-- impl/
|   |
|   +-- entrenamiento_live/
|   |   +-- __init__.py
|   |   +-- timer_task.py
|   |   +-- coach_task.py
|   |
|   +-- excepciones/
|       +-- __init__.py
|       +-- kickboxing_exception.py
|
+-- main_kickboxing.py             # Nuevo punto de entrada
+-- README_kick.md                 # Este archivo
+-- data/                          # Datos persistidos
```

---

## Módulos del Sistema

-   **`entidades`**: Contiene los DTOs como `Movimiento`, `SesionDeEntrenamiento`, `PerfilDeLuchador`. Sin lógica de negocio.
-   **`servicios`**: Orquesta la lógica de negocio. `ServicioEntrenamiento` inicia y gestiona sesiones, `ServicioSalud` aplica recomendaciones.
-   **`patrones`**: Implementaciones genéricas y concretas de los patrones de diseño (Factory, Strategy, Observer, Singleton).
-   **`entrenamiento_live`**: Componentes concurrentes (hilos) que simulan el entrenamiento en tiempo real, como `TimerTask` y `CoachTask`.
-   **`excepciones`**: Excepciones personalizadas para un manejo de errores de dominio específico.

---

## Documentación Técnica

-   **Convenciones**: PEP 8, Docstrings de Google, y Type Hints son mandatorios.
-   **Constantes**: Todos los valores mágicos (duración de round, calorías por movimiento, etc.) deben estar en `constantes.py`.
-   **Excepciones**: Se debe usar un manejo de excepciones robusto con clases personalizadas que hereden de `KickboxingException`.

---

## Testing y Validación

-   **Tests Unitarios**: Se deben crear tests para cada componente, especialmente:
    -   `test_movimiento_factory.py`: Verifica que el factory crea todos los tipos de movimientos correctamente.
    -   `test_patrones.py`: Valida la correcta implementación de cada patrón (ej. que `PerfilDeLuchador` sea un Singleton).
    -   `test_estrategias.py`: Prueba cada algoritmo de `Strategy` con datos de entrada conocidos.
-   **Test de Integración**: El `main_kickboxing.py` actúa como un test de integración que ejecuta un flujo completo.
-   **Validación Manual**: Ejecutar `python main_kickboxing.py` y verificar que no haya errores y que el archivo `.dat` del perfil se cree/actualice.

---

## Contribución

### Cómo Agregar un Nuevo Movimiento (Ej: "Rodillazo Volador")

1.  **Constantes.py**:
    ```python
    POTENCIA_RODILLAZO_VOLADOR = 75
    CALORIAS_RODILLAZO_VOLADOR = 25
    ```
2.  **Entidad**: Crear `entidades/movimientos/rodillazo_volador.py`
    ```python
    from .movimiento import Movimiento
    from ...constantes import POTENCIA_RODILLAZO_VOLADOR, CALORIAS_RODILLAZO_VOLADOR

    class RodillazoVolador(Movimiento):
        def __init__(self):
            super().__init__(nombre="Rodillazo Volador", potencia=POTENCIA_RODILLAZO_VOLADOR, calorias=CALORIAS_RODILLAZO_VOLADOR)
    ```
3.  **Factory**: Actualizar `patrones/factory/movimiento_factory.py`
    ```python
    from ...entidades.movimientos.rodillazo_volador import RodillazoVolador

    class MovimientoFactory:
        @staticmethod
        def crear_movimiento(tipo: str) -> Movimiento:
            # ... otros casos
            elif tipo == "RodillazoVolador":
                return RodillazoVolador()
            else:
                raise ValueError(f"Movimiento desconocido: {tipo}")
    ```
4.  **Uso**:
    ```python
    nuevo_movimiento = MovimientoFactory.crear_movimiento("RodillazoVolador")
    ```

---

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
