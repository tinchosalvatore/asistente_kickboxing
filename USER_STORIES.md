# Historias de Usuario - Asistente de Entrenamiento de Kickboxing

**Proyecto**: Kickboxing Assistant
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestión del Perfil y Sesiones](#epic-1-gestión-del-perfil-y-sesiones)
2. [Epic 2: Gestión de Movimientos y Combinaciones](#epic-2-gestión-de-movimientos-y-combinaciones)
3. [Epic 3: Entrenamiento Interactivo en Tiempo Real](#epic-3-entrenamiento-interactivo-en-tiempo-real)
4. [Epic 4: Gestión de Salud y Nutrición](#epic-4-gestión-de-salud-y-nutrición)
5. [Epic 5: Orquestación y Evaluación del Entrenamiento](#epic-5-orquestación-y-evaluación-del-entrenamiento)
6. [Epic 6: Persistencia y Seguimiento del Progreso](#epic-6-persistencia-y-seguimiento-del-progreso)
7. [Historias Técnicas (Patrones de Diseño)](#historias-técnicas-patrones-de-diseño)

---

## Epic 1: Gestión del Perfil y Sesiones

### US-001: Crear Perfil de Atleta

**Como** nuevo usuario,
**Quiero** crear un perfil con mi nombre, peso y altura,
**Para** que el sistema pueda personalizar mis entrenamientos y cálculos de métricas.

#### Criterios de Aceptación
- [ ] El sistema debe permitir crear un `PerfilDeLuchador` con: nombre, peso (kg), altura (cm).
- [ ] El peso y la altura deben ser números positivos; de lo contrario, lanzar `ValueError`.
- [ ] El perfil se gestionará a través de un Singleton para garantizar una única instancia.

#### Detalles Técnicos
**Clase**: `PerfilDeLuchador` (`entidades/perfil_atleta.py`)
**Servicio**: `KickboxingServiceRegistry` (`servicios/kickboxing_service_registry.py`)

**Código de ejemplo**:
```python
from python_kickboxing_assistant.servicios.kickboxing_service_registry import KickboxingServiceRegistry

registry = KickboxingServiceRegistry.get_instance()
perfil = registry.get_perfil()
perfil.set_nombre("Rocky Balboa")
perfil.set_peso(80.5)
perfil.set_altura(180)
```

**Validaciones**:
```python
perfil.set_peso(-70)  # Lanza ValueError: El peso debe ser positivo.
```

**Trazabilidad**: `main_kickboxing.py` (demostración inicial)

---

### US-002: Iniciar una Sesión de Entrenamiento

**Como** atleta,
**Quiero** iniciar una sesión de entrenamiento especificando el tipo (ej. "Saco Pesado") y un objetivo (ej. "Quemar Calorías"),
**Para** realizar un entrenamiento estructurado y enfocado.

#### Criterios de Aceptación
- [ ] Una `SesionDeEntrenamiento` debe tener: un tipo, una referencia al perfil del atleta, una lista de movimientos (vacía al inicio) y una `EvaluacionStrategy`.
- [ ] La estrategia de evaluación debe ser inyectada al crear la sesión.

#### Detalles Tecnicos
**Clase**: `SesionDeEntrenamiento` (`entidades/sesion_entrenamiento.py`)
**Servicio**: `ServicioEntrenamiento`

**Código de ejemplo**:
```python
from python_kickboxing_assistant.servicios.servicio_entrenamiento import ServicioEntrenamiento
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_de_calorias import EstrategiaDeCalorias

servicio_ent = ServicioEntrenamiento()
sesion = servicio_ent.iniciar_sesion(
    tipo="Saco Pesado",
    atleta=perfil,
    estrategia_evaluacion=EstrategiaDeCalorias()
)
```

**Trazabilidad**: `main_kickboxing.py`

---

## Epic 2: Gestión de Movimientos y Combinaciones

### US-003: Registrar un Jab en la Sesión

**Como** atleta,
**Quiero** que el sistema registre la ejecución de un "Jab",
**Para** que cuente en las métricas de mi sesión actual.

#### Criterios de Aceptación
- [ ] Los `Jab` deben ser creados exclusivamente a través de `MovimientoFactory`.
- [ ] Cada `Jab` tiene valores predefinidos de potencia y calorías definidos en `constantes.py`.
- [ ] El movimiento creado se añade a la lista de movimientos de la `SesionDeEntrenamiento` activa.

#### Detalles Tecnicos
**Clase**: `Jab` (`entidades/movimientos/jab.py`)
**Factory**: `MovimientoFactory` (`patrones/factory/movimiento_factory.py`)

**Código de ejemplo**:
```python
from python_kickboxing_assistant.patrones.factory.movimiento_factory import MovimientoFactory

movimiento_jab = MovimientoFactory.crear_movimiento("Jab")
sesion.agregar_movimiento(movimiento_jab)
```

**Constantes utilizadas**:
```python
# en constantes.py
POTENCIA_JAB = 10
CALORIAS_JAB = 1
```

---

### US-004: Registrar una Patada Baja (Low Kick)

**Como** atleta,
**Quiero** que el sistema registre la ejecución de una "LowKick",
**Para** incluir movimientos de pierna en mi entrenamiento.

#### Criterios de Aceptación
- [ ] Las `LowKick` deben ser creadas exclusivamente a través de `MovimientoFactory`.
- [ ] Tienen valores de potencia y calorías superiores a los de un `Jab`.

#### Detalles Tecnicos
**Clase**: `LowKick` (`entidades/movimientos/low_kick.py`)
**Factory**: `MovimientoFactory`

**Código de ejemplo**:
```python
movimiento_kick = MovimientoFactory.crear_movimiento("LowKick")
sesion.agregar_movimiento(movimiento_kick)
```

**Constantes utilizadas**:
```python
# en constantes.py
POTENCIA_LOW_KICK = 35
CALORIAS_LOW_KICK = 8
```

---

## Epic 3: Entrenamiento Interactivo en Tiempo Real

### US-005: Controlar el Tiempo del Round

**Como** sistema de entrenamiento,
**Quiero** correr un temporizador en un hilo que notifique el inicio y fin de cada round,
**Para** guiar el entrenamiento en tiempo real.

#### Criterios de Aceptación
- [ ] El `TimerTask` debe ejecutarse en un hilo separado (`threading.Thread`).
- [ ] Debe ser un `Observable` que notifica a sus `Observer` con eventos como "INICIO_ROUND" y "FIN_ROUND".
- [ ] Debe poder detenerse de forma segura (`graceful shutdown`) con un `threading.Event`.

#### Detalles Tecnicos
**Clase**: `TimerTask` (`entrenamiento_live/timer_task.py`)
**Patrón**: Observer (Observable)

**Código de ejemplo**:
```python
from python_kickboxing_assistant.entrenamiento_live.timer_task import TimerTask

controlador = ControladorDeSesion() # Es un Observer
timer = TimerTask(duracion_round=180, duracion_descanso=60)
timer.agregar_observador(controlador)
timer.start()
# ...después
timer.detener()
timer.join()
```

**Constantes utilizadas**:
```python
# en constantes.py
DURACION_ROUND_SEGUNDOS = 180
DURACION_DESCANSO_SEGUNDOS = 60
```

---

### US-006: Guiar con un Coach Virtual

**Como** sistema de entrenamiento,
**Quiero** tener un "Coach" en un hilo que "cante" combinaciones a intervalos,
**Para** que el atleta reciba una guía activa y dinámica.

#### Criterios de Aceptación
- [ ] El `CoachTask` debe ejecutarse en un hilo separado.
- [ ] Debe ser un `Observable` que notifica a sus `Observer` con un evento `NUEVA_COMBINACION`, pasando la combinación como payload.
- [ ] Las combinaciones deben ser seleccionadas de un repertorio predefinido en `constantes.py`.

#### Detalles Tecnicos
**Clase**: `CoachTask` (`entrenamiento_live/coach_task.py`)
**Patrón**: Observer (Observable)

**Código de ejemplo**:
```python
from python_kickboxing_assistant.entrenamiento_live.coach_task import CoachTask

coach = CoachTask()
coach.agregar_observador(controlador_de_sesion) # El controlador también observa al coach
coach.start()
```

---

## Epic 4: Gestión de Salud y Nutrición

### US-007: Analizar Salud Post-Sparring

**Como** analizador de salud,
**Quiero** ser notificado cuando termina una sesión de sparring,
**Para** evaluar el impacto y actualizar el estado de salud del atleta.

#### Criterios de Aceptación
- [ ] El `AnalizadorDeSalud` debe implementar la interfaz `Observer`.
- [ ] Debe suscribirse a las sesiones de tipo `Sparring`.
- [ ] Al recibir la notificación `FIN_SESION`, debe usar una `RecomendacionSaludStrategy` para determinar la acción a seguir.
- [ ] Debe actualizar el `estado_salud` en el `PerfilDeLuchador`.

#### Detalles Tecnicos
**Clase**: `AnalizadorDeSalud` (`servicios/servicio_salud.py`)
**Patrones**: Observer, Strategy

**Código de ejemplo**:
```python
analizador = AnalizadorDeSalud()
sesion_sparring.agregar_observador(analizador)

# Al finalizar la sesión, el analizador se activa automáticamente
servicio_entrenamiento.finalizar_sesion(sesion_sparring)

# El perfil ahora reflejará el nuevo estado de salud
print(perfil.get_estado_salud()) # Ej: "Descanso Moderado"
```

---

### US-008: Sugerir Comida Post-Entrenamiento

**Como** sistema,
**Quiero** sugerir una comida apropiada después de cada sesión,
**Para** que el atleta optimice su recuperación.

#### Criterios de Aceptación
- [ ] La sugerencia debe basarse en la intensidad y duración de la sesión finalizada.
- [ ] Debe usar el patrón `Strategy` con diferentes implementaciones (`EstrategiaComidaLigera`, `EstrategiaComidaRecuperacion`).
- [ ] El `ServicioEntrenamiento` es responsable de orquestar esta acción al finalizar una sesión.

#### Detalles Tecnicos
**Interfaz**: `SugerenciaComidaStrategy` (`patrones/strategy/comida_strategy.py`)
**Servicio**: `ServicioEntrenamiento`

**Código de ejemplo**:
```python
# Esta lógica estaría dentro de servicio_entrenamiento.finalizar_sesion()
if sesion.get_intensidad() > 7:
    estrategia_comida = EstrategiaComidaRecuperacion()
else:
    estrategia_comida = EstrategiaComidaLigera()

sugerencia = estrategia_comida.sugerir(sesion)
print(f"Comida sugerida: {sugerencia.get_nombre()}")
```

---

## Epic 5: Orquestación y Evaluación del Entrenamiento

### US-009: Evaluar Sesión de Entrenamiento

**Como** atleta,
**Quiero** que mi sesión de entrenamiento sea evaluada según mi objetivo,
**Para** saber si cumplí mi meta (ej. quemar X calorías).

#### Criterios de Aceptación
- [ ] La evaluación se realiza al finalizar la sesión.
- [ ] El `ServicioEntrenamiento` delega el cálculo al objeto `EvaluacionStrategy` que fue inyectado en la sesión.
- [ ] El resultado (ej. `{"tipo": "Calorías", "valor": 520}`) se almacena en el objeto `SesionDeEntrenamiento`.

#### Detalles Tecnicos
**Servicio**: `ServicioEntrenamiento.finalizar_sesion()`
**Patrón**: Strategy

**Salida esperada**:
```
Evaluando sesión...
Resultado: Calorías = 520.0 kcal
```

---

## Epic 6: Persistencia y Seguimiento del Progreso

### US-010: Persistir Perfil del Atleta

**Como** sistema,
**Quiero** guardar el objeto `PerfilDeLuchador` en disco,
**Para** mantener el progreso del atleta entre diferentes usos de la aplicación.

#### Criterios de Aceptación
- [ ] Debe serializar el objeto `PerfilDeLuchador` completo usando `Pickle`.
- [ ] El archivo debe guardarse en el directorio `data/` con el formato `{nombre_atleta}.dat`.
- [ ] Debe manejar `PersistenciaException` si ocurre un error de E/S.

#### Detalles Tecnicos
**Servicio**: `ServicioPerfil.persistir()`

**Código de ejemplo**:
```python
servicio_perfil = ServicioPerfil()
try:
    servicio_perfil.persistir(perfil)
    print("Perfil guardado exitosamente.")
except PersistenciaException as e:
    print(f"Error al guardar: {e}")
```

---

### US-011: Recuperar Perfil del Atleta

**Como** sistema,
**Quiero** cargar un perfil de atleta desde el disco al iniciar,
**Para** continuar con el progreso guardado previamente.

#### Criterios de Aceptación
- [ ] Debe deserializar el archivo `.dat` para reconstruir el objeto `PerfilDeLuchador`.
- [ ] Debe manejar `PersistenciaException` si el archivo no existe o está corrupto.

#### Detalles Tecnicos
**Servicio**: `ServicioPerfil.recuperar()`

**Código de ejemplo**:
```python
try:
    perfil_cargado = ServicioPerfil.recuperar("Rocky Balboa")
    print("Perfil cargado.")
except PersistenciaException as e:
    print(f"No se pudo cargar el perfil: {e}")
```

---

## Historias Técnicas (Patrones de Diseño)

(Estas historias replican las del `README_kick.md` para mantener la consistencia y el detalle técnico en este documento también)

### US-TECH-001: Implementar Singleton para el Service Registry

**Como** arquitecto de software,
**Quiero** garantizar una única instancia del `KickboxingServiceRegistry`,
**Para** tener un punto de acceso global y consistente a los servicios y al perfil del atleta.

#### Criterios de Aceptación
- [ ] Implementar el patrón Singleton de forma thread-safe usando `threading.Lock` y double-checked locking.
- [ ] Proveer un método `get_instance()` para el acceso.

---

### US-TECH-002: Implementar Factory Method para Movimientos

**Como** arquitecto de software,
**Quiero** centralizar la creación de `Movimiento` usando el patrón Factory Method,
**Para** desacoplar el código cliente de las clases concretas de movimientos.

#### Criterios de Aceptación
- [ ] Crear una clase `MovimientoFactory` con un método estático `crear_movimiento`.
- [ ] Usar un diccionario de constructores para evitar `if/elif`.
- [ ] Lanzar `ValueError` si el tipo de movimiento es desconocido.

---

### US-TECH-003: Implementar Observer para Eventos en Tiempo Real

**Como** arquitecto de software,
**Quiero** implementar el patrón Observer con Generics (`Observable[T]`, `Observer[T]`),
**Para** notificar eventos de los hilos (`TimerTask`, `CoachTask`) de forma tipo-segura y desacoplada.

#### Criterios de Aceptación
- [ ] Crear las clases base `Observable[T]` y `Observer[T]`.
- [ ] `TimerTask` debe ser `Observable[str]`.
- [ ] `ControladorDeSesion` debe ser `Observer[str]`.

---

### US-TECH-004: Implementar Strategy para Algoritmos Intercambiables

**Como** arquitecto de software,
**Quiero** usar el patrón Strategy para la evaluación de sesiones, sugerencias de comida y recomendaciones de salud,
**Para** permitir que estos algoritmos sean intercambiables y extensibles.

#### Criterios de Aceptación
- [ ] Crear interfaces `ABC` para cada familia de estrategias (`EvaluacionStrategy`, etc.).
- [ ] Implementar al menos dos estrategias concretas para cada interfaz.
- [ ] Los servicios deben recibir la estrategia a usar vía inyección de dependencias.

---

### US-TECH-005: Implementar Registry para Dispatch Polimórfico

**Como** arquitecto de software,
**Quiero** usar el patrón Registry dentro del `KickboxingServiceRegistry`,
**Para** evitar el uso de `isinstance()` al aplicar operaciones específicas a diferentes tipos de `Movimiento`.

#### Criterios de Aceptación
- [ ] El `KickboxingServiceRegistry` debe tener diccionarios de manejadores (handlers).
- [ ] Crear un método (ej. `mostrar_movimiento`) que use el registro para despachar la llamada al método correcto según el tipo de `Movimiento`.

---
