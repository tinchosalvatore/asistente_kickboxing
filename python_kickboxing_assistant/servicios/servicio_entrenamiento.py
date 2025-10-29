from typing import Type
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.patrones.strategy.evaluacion_strategy import EvaluacionStrategy
from python_kickboxing_assistant.patrones.strategy.comida_strategy import ComidaStrategy
from python_kickboxing_assistant.entrenamiento_live.timer_task import TimerTask
from python_kickboxing_assistant.entrenamiento_live.coach_task import CoachTask
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_recuperacion import EstrategiaComidaRecuperacion
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_comida_ligera import EstrategiaComidaLigera


class ServicioEntrenamiento:
    """
    Servicio para gestionar las sesiones de entrenamiento.
    """

    def iniciar_sesion(self, tipo: str, atleta: PerfilDeLuchador,
                         estrategia_evaluacion: EvaluacionStrategy) -> SesionDeEntrenamiento:
        """
        Inicia una nueva sesión de entrenamiento.
        """
        return SesionDeEntrenamiento(tipo, atleta, estrategia_evaluacion)

    def ejecutar_sesion_en_vivo(self, sesion: SesionDeEntrenamiento, duracion_segundos: int):
        """
        Ejecuta una sesión de entrenamiento en vivo con un Timer y un Coach.
        """
        print(f"Iniciando sesión de {sesion.tipo} para {sesion.atleta.nombre}...")

        timer = TimerTask(duracion_round=duracion_segundos)
        coach = CoachTask(sesion)

        timer.agregar_observador(coach)

        timer.start()
        coach.start()

        timer.join()
        coach.detener()
        coach.join()

        print("La sesión en vivo ha terminado.")

    def finalizar_sesion(self, sesion: SesionDeEntrenamiento):
        """
        Finaliza una sesión de entrenamiento y realiza la evaluación.
        """
        sesion.evaluar()
        print("Sesión finalizada y evaluada.")

    def obtener_sugerencia_comida(self, sesion: SesionDeEntrenamiento) -> ComidaStrategy:
        """
        Obtiene una sugerencia de comida basada en la intensidad de la sesión.
        """
        # Lógica simple para determinar la estrategia de comida
        if sesion.get_resultado_evaluacion().get('valor', 0) > 500:  # Umbral de ejemplo
            return EstrategiaComidaRecuperacion()
        else:
            return EstrategiaComidaLigera()
