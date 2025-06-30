# TrabajoFinal_LDP
Trabajo Final 
# Juego de Piedra, Papel o Tijera

Este proyecto es una versión interactiva del clásico juego de Piedra, Papel o Tijera, desarrollada en Python. Permite jugar contra la computadora o entre dos jugadores, e incluye un historial de resultados y estadísticas finales al salir del juego.

Características 

Modo un jugador: compite contra la computadora.
Modo multijugador: dos personas pueden jugar, una contra otra.
Historial de resultados: se guarda el resultado de cada partida.
Estadísticas: resumen final de partidas ganadas, perdidas y empatadas.
Menú interactivo: navegación fácil y clara desde la consola.
Validación de entradas: asegura que las opciones elegidas sean válidas.

#Variables
- `mostrar_menu()`  
  Muestra el menú principal del juego.

- `reglas()`  
  Explica las reglas básicas del juego.

- `jugar()`  
  Permite elegir entre el modo contra la PC o multijugador.

- `jugar_PC()`  
  Implementa el juego contra la computadora.

- `multijugador()`  
  Implementa el juego entre dos jugadores.

- `guardar_resultado(resultado)`  
  Almacena el resultado de cada ronda en la lista `historial_resultados`.

- `mostrar_resumen()`  
  Muestra un resumen estadístico al finalizar el juego.

#Reglas del juego

- Piedra gana a Tijera
- Tijera gana a Papel
- Papel gana a Piedra
- Si ambos jugadores eligen la misma opción, es empate.

#Requisitos

- Python 

#Cómo jugar

1. Ejecuta el script en un entorno que soporte Python como Visual Studio.
2. Ingresa tu nombre o alias.
3. Elige una opción del menú:
   - 1: Jugar (contra la PC o con otra persona).
   - 2: Ver las reglas del juego.
   - 3: Salir del juego y ver el resumen de resultados.

#Autora

Este juego fue desarrollado con fines educativos y de entretenimiento, como un ejercicio para la materia de lógica de programación.
