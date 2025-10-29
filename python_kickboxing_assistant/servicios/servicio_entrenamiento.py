from typing import Type
import time
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.patrones.strategy.comida_strategy import ComidaStrategy
from python_kickboxing_assistant.entrenamiento_live.timer_task import TimerTask
from python_kickboxing_assistant.entrenamiento_live.coach_task import CoachTask
from python_kickboxing_assistant.entrenamiento_live.luchador_task import LuchadorTask
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_recuperacion import EstrategiaComidaRecuperacion
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_ligera import EstrategiaComidaLigera
from python_kickboxing_assistant.servicios.servicio_salud import AnalizadorDeSalud
from python_kickboxing_assistant.excepciones.kickboxing_exception import AtletaNoAptoException


class ServicioEntrenamiento:
    """
    Servicio para gestionar las sesiones de entrenamiento.
    """

    def iniciar_sesion(self, tipo: str, atleta: PerfilDeLuchador,
                         estrategia_evaluacion: EvaluacionStrategy) -> SesionDeEntrenamiento:
        """
        Inicia una nueva sesión de entrenamiento.
        Verifica la aptitud del atleta y suscribe observadores relevantes.
        """
        # Tarea 3.2: Usar la excepción AtletaNoAptoException
        if atleta.get_estado_salud() != "Óptimo":
            raise AtletaNoAptoException(f"El atleta {atleta.get_nombre()} no está 'Óptimo'. Estado actual: {atleta.get_estado_salud()}")

        sesion = SesionDeEntrenamiento(tipo, atleta, estrategia_evaluacion)

        # Tarea 1.2: Suscribir el observador de salud para sesiones de Sparring
        if sesion.tipo == "Sparring":
            analizador = AnalizadorDeSalud()
            sesion.agregar_observador(analizador)
            print("[ServicioEntrenamiento] AnalizadorDeSalud suscrito a la sesión de Sparring.")

        return sesion

    def ejecutar_sesion_en_vivo(self, sesion: SesionDeEntrenamiento, duracion_total_segundos: int, duracion_round: int = None, duracion_descanso: int = None):
        """
        Ejecuta una sesión de entrenamiento en vivo con un Timer y un Coach.
        La sesión durará duracion_total_segundos.
        """
        print(f"Iniciando sesión de {sesion.tipo} para {sesion.atleta.nombre} durante {duracion_total_segundos} segundos...")

        # Pasa las duraciones específicas si se proporcionan, de lo contrario usa los valores por defecto de TimerTask
        timer_args = {}
        if duracion_round is not None:
            timer_args['duracion_round'] = duracion_round
        if duracion_descanso is not None:
            timer_args['duracion_descanso'] = duracion_descanso

        timer = TimerTask(**timer_args)
        threads_to_manage = [timer]

        if sesion.tipo == "Sparring":
            coach = CoachTask(sesion, es_sparring=True)
            luchador1 = LuchadorTask("Luchador 1", sesion)
            luchador2 = LuchadorTask("Luchador 2", sesion)

            timer.agregar_observador(coach)
            timer.agregar_observador(luchador1)
            timer.agregar_observador(luchador2)

            threads_to_manage.extend([coach, luchador1, luchador2])
        else:
            coach = CoachTask(sesion)
            timer.agregar_observador(coach)
            threads_to_manage.append(coach)

        for t in threads_to_manage:
            t.start()

        # Esperar la duración total de la sesión
        time.sleep(duracion_total_segundos)

        # Detener los hilos de forma segura
        for t in threads_to_manage:
            t.detener()

        for t in threads_to_manage:
            t.join()

        print("La sesión en vivo ha terminado.")

    def finalizar_sesion(self, sesion: SesionDeEntrenamiento):
        """
        Finaliza una sesión de entrenamiento, realiza la evaluación
        y notifica a los observadores.
        """
        sesion.evaluar()
        print("Sesión evaluada.")
        
        # Tarea 1.2: Notificar a los observadores (como AnalizadorDeSalud)
        sesion.finalizar()
        print("Observadores notificados de la finalización de la sesión.")

    def obtener_sugerencia_comida(self, sesion: SesionDeEntrenamiento) -> ComidaStrategy:
        """
        Obtiene una sugerencia de comida basada en la intensidad de la sesión.
        """
        # Lógica simple para determinar la estrategia de comida
        if sesion.get_resultado_evaluacion().get('valor', 0) > 500:  # Umbral de ejemplo
            return EstrategiaComidaRecuperacion()
        else:
            return EstrategiaComidaLigera()
