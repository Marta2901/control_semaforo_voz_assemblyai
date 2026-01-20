##---IMPORTACIONES: TRAER FUNCIONES DE LOS MÓDULOS
#Importa: función que crea la interfaz gráfica
from modules.gui_manager import crear_ventana
#Importa: función que graba, sube y transcribe audio
from modules.audio_manager import escuchar
#Importa: función que procesa comandos
from modules.command_processor import procesar_comandos
#Tkinter para widgets adicionales si es necesario
import tkinter as tk

##---FUNCIÓN PRINCIPAL: main()
def main():
    """
    Función principal que orquesta toda la aplicación.
    Flujo:
        1. Crear la interfaz gráfica
        2. Obtener referencias a todos los widgets
        3. Definir función que se ejecuta al pulsar botón
        4. Crear botón "Escuchar"
        5. Iniciar bucle de eventos
    """
    ##---PASO 1: CREAR INTERFAZ GRÁFICA
    #LLama a la función que crea toda la GUI
    #Retorna todos los widgets necesarios
    (ventana, canvas, rojo, amarillo, verde, texto_label,
     resultado_label) = crear_ventana()
    
    ##---PASO2: DEFINIR FUNCIÓN DEL BOTÓN
    def ejecutar_reconocimiento():
        """
        Se ejecuta automáticamente al pulsar el botón "Escuchar".
        
        Flujo:
            1. Cambiar texto a "Escuchando..."
            2. Actualizar interfaz (ventana.update())
            3. Grabar y transcribir audio
            4. Cambiar texto a "Procesando..."
            5. Procesar el comando reconocido
            6. Actualizar semáforo según el comando
        """
        # Cambiar etiqueta a "Escuchando..."
        texto_label.config(text=" Escuchando... Habla ahora")
        #Fuerza a Tkinter a dibujar los cambios inmediatamente
        ventana.update()

        ##---GRABAR, SUBIR Y TRANSCRIBIR CON ASSEMBLYAI
        # Llama a la función escuchar() del módulo audio_manager.py
        # Esta función hace TODO: grabar → subir → transcribir → polling
        text = escuchar()

        ##---MOSTRAR LO QUE EL SISTEMA INTERPRETÓ
        #Actualiza la etiqueta con el texto reconocido
        if text:
            # Si hay texto transcrito, mostrarlo
            texto_label.config(text=f"Interpretado: {text}")
        else:
            # Si no hay texto (error o silencio)
            texto_label.config(text="No se entendió, intenta de nuevo...")
        
        #Actualiza la interfaz para mostrar el texto transcrito
        ventana.update()

        ##---PROCESAR COMAND Y ACTUALIZAR SEMÁFORO
        #Llama a la función que interpreta el comando
        procesar_comandos(
            text,                       #Texto transcrito
            canvas,                     #Canvas del semáforo
            (rojo, amarillo, verde),    #IDs de las luces
            resultado_label,            #Etiqueta de resultado
            ventana                     #Ventana(para cerrar si fuera necesario)
        )

    ##---PASO 3: CREAR BOTÓN "ESCUCHAR"
    boton = tk.Button(
        ventana, # Contenedor padre
        text=" Escuchar", # Texto del botón
        command=ejecutar_reconocimiento, # Función que se ejecuta al hacer clic
        font=("Arial", 14), # Fuente: Arial tamaño 14
        bg="#00ffcc", # Fondo: cian
        fg="black", # Texto: negro
        width=15, # Ancho: 15 caracteres
        height=2 # Alto: 2 líneas
    )
    #Coloca el botón con 20 píxeles de espacio vertical
    boton.pack(pady=20)

    ##---PASO 4: INICIAR BUCLE DE EVENTOS (MAINLOOP)
    # mainloop() es FUNDAMENTAL en cualquier aplicación Tkinter
    # Mantiene la ventana abierta y escucha eventos del usuario
    # Bloquea la ejecución hasta que se cierre la ventana
    ventana.mainloop()

##---PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    # Este bloque se ejecuta SOLO si este archivo se ejecuta directamente
    # NO se ejecuta si el archivo se importa como módulo en otro programa
    # Esto es una buena práctica en Python
    main() #Llama a la función principal