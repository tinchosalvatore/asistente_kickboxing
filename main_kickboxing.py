from python_kickboxing_assistant.servicios.kickboxing_service_registry import KickboxingServiceRegistry
from python_kickboxing_assistant.servicios.servicio_entrenamiento import ServicioEntrenamiento
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_de_calorias import EstrategiaDeCalorias
from python_kickboxing_assistant.servicios.servicio_perfil import ServicioPerfil

def main():
    """
    Función principal que demuestra el flujo de una sesión de entrenamiento de kickboxing.
    """
    # 1. Obtener la instancia del registro de servicios (Singleton)
    registry = KickboxingServiceRegistry()

    # 2. Obtener el perfil del atleta
    perfil = registry.get_perfil()
    print(f"Perfil cargado para: {perfil.nombre}")

    # 3. Iniciar servicio de entrenamiento
    servicio_entrenamiento = ServicioEntrenamiento()

    # 4. Crear una sesión de Saco Pesado con estrategia de calorías
    print("\nIniciando una nueva sesión de entrenamiento...")
    sesion = servicio_entrenamiento.iniciar_sesion(
        tipo="Saco Pesado",
        atleta=perfil,
        estrategia_evaluacion=EstrategiaDeCalorias()
    )

    # 5. Iniciar el entrenamiento en vivo (Observer)
    # Esto iniciará los hilos del Timer y el Coach Virtual
    # que "cantan" movimientos. El Factory los crea internamente.
    servicio_entrenamiento.ejecutar_sesion_en_vivo(sesion, duracion_segundos=10) # Duración corta para la demo

    # 6. Finalizar y evaluar
    servicio_entrenamiento.finalizar_sesion(sesion)
    resultado_evaluacion = sesion.get_resultado_evaluacion()
    print(f"Resultado de la evaluación (Calorías): {resultado_evaluacion.get('valor', 0)}")


    # 7. Obtener sugerencia de comida (Strategy)
    sugerencia = servicio_entrenamiento.obtener_sugerencia_comida(sesion)
    print(f"Sugerencia de comida post-entrenamiento: {sugerencia.get_nombre()}")
    sugerencia.preparar()


    # 8. Persistir el progreso
    servicio_perfil = ServicioPerfil()
    servicio_perfil.persistir(perfil)
    print(f"\nPerfil de {perfil.nombre} guardado con éxito.")

if __name__ == "__main__":
    main()
