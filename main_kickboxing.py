import json
from datetime import datetime
from python_kickboxing_assistant.servicios.kickboxing_service_registry import KickboxingServiceRegistry
from python_kickboxing_assistant.servicios.servicio_entrenamiento import ServicioEntrenamiento
from python_kickboxing_assistant.patrones.strategy.impl.estrategia_de_calorias import EstrategiaDeCalorias
from python_kickboxing_assistant.servicios.servicio_perfil import ServicioPerfil
from python_kickboxing_assistant.entidades.perfil_atleta import PerfilDeLuchador
from python_kickboxing_assistant.entidades.sesion_entrenamiento import SesionDeEntrenamiento
from python_kickboxing_assistant.entidades.nutricion import Comida


def guardar_resumen_json(perfil: PerfilDeLuchador, sesion: SesionDeEntrenamiento, comida_sugerida: Comida):
    """
    Guarda un resumen de la sesión en un archivo JSON en la carpeta data/.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # La ruta debe ser relativa al directorio raíz del proyecto para el guardado.
    filename = f"data/{perfil.nombre.replace(' ', '_')}_{sesion.tipo.replace(' ', '_')}_{timestamp}.json"

    resumen = {
        "atleta": perfil.nombre,
        "sesion_tipo": sesion.tipo,
        "fecha_hora": datetime.now().isoformat(),
        "evaluacion": sesion.get_resultado_evaluacion(),
        "sugerencia_nutricional": {
            "nombre": comida_sugerida.get_nombre(),
            "descripcion": comida_sugerida.descripcion
        },
        "estado_salud_post_sesion": perfil.get_estado_salud()
    }

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(resumen, f, ensure_ascii=False, indent=4)
        print(f"Resumen de la sesión guardado en: {filename}")
    except IOError as e:
        print(f"Error al guardar el resumen JSON: {e}")


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
    servicio_entrenamiento.ejecutar_sesion_en_vivo(sesion)

    # 6. Finalizar y evaluar
    servicio_entrenamiento.finalizar_sesion(sesion)
    resultado_evaluacion = sesion.get_resultado_evaluacion()
    print(f"Resultado de la evaluación (Calorías): {resultado_evaluacion.get('valor', 0)}")

    # 7. Obtener sugerencia de comida y guardar resumen JSON
    estrategia_comida = servicio_entrenamiento.obtener_sugerencia_comida(sesion)
    comida_sugerida = estrategia_comida.sugerir(sesion)
    print(f"Sugerencia de comida post-entrenamiento: {comida_sugerida.get_nombre()}")
    print(f"Descripción: {comida_sugerida.descripcion}")
    guardar_resumen_json(perfil, sesion, comida_sugerida)

    # --- Demostración de Sesión de Sparring ---
    print("\n--- Iniciando Sesión de Sparring ---")
    sesion_sparring = servicio_entrenamiento.iniciar_sesion(
        tipo="Sparring",
        atleta=perfil,
        estrategia_evaluacion=EstrategiaDeCalorias()
    )
    servicio_entrenamiento.ejecutar_sesion_en_vivo(sesion_sparring)
    servicio_entrenamiento.finalizar_sesion(sesion_sparring)
    resultado_evaluacion_sparring = sesion_sparring.get_resultado_evaluacion()
    print(f"Resultado de la evaluación de Sparring (Calorías): {resultado_evaluacion_sparring.get('valor', 0)}")

    # Obtener sugerencia de comida para sparring y guardar resumen JSON
    estrategia_comida_sparring = servicio_entrenamiento.obtener_sugerencia_comida(sesion_sparring)
    comida_sugerida_sparring = estrategia_comida_sparring.sugerir(sesion_sparring)
    print(f"Sugerencia de comida post-sparring: {comida_sugerida_sparring.get_nombre()}")
    print(f"Descripción: {comida_sugerida_sparring.descripcion}")
    guardar_resumen_json(perfil, sesion_sparring, comida_sugerida_sparring)

    # 8. Persistir el progreso (.dat)
    servicio_perfil = ServicioPerfil()
    servicio_perfil.persistir(perfil)
    print(f"\nPerfil de {perfil.nombre} guardado con éxito en formato .dat.")


if __name__ == "__main__":
    main()
