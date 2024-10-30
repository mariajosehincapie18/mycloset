Esta aplicación está diseñada para hacer la vida más sencilla, brindando a las personas una visión general de su armario. Ofrece una lista completa de todas las prendas, organizadas por categorías, junto con funciones adicionales como:
Combinación de outfits: Facilita la creación de conjuntos de ropa.
Recomendaciones de outfits: Sugiere combinaciones basadas en las prendas disponibles tomando en cuenta los gustos evaluados en la caracterización del perfil de cada .
Encuestas de estado de las prendas: Ayuda a evaluar si las prendas están listas para usarse.
El objetivo principal es abordar la necesidad de tener una visión general del armario, permitiendo a los usuarios aprovechar mejor su ropa y hacer la mejor combinación de outfits de forma diaria. Esto simplifica la tarea de elegir qué ponerse y optimiza el uso de todas las prendas disponibles.

Requisitos Funcionales 
1.	Perfil de Usuario:
	El sistema debe permitir a los usuarios crear un perfil personal, que incluya información como:
	Nombre.
	Preferencias de estilo (formal, casual, deportivo).
	Colores preferidos.
	Combinaciones de colores preferidos
	Tipos de ropa favoritos (vestidos, pantalones, camisetas).
	Los usuarios deben poder modificar sus preferencias y ajustar su perfil en cualquier momento.
	El sistema debe utilizar esta información para personalizar las recomendaciones de outfits y el orden de prioridad de las prendas.

2.	Gestión de Prendas:
	El sistema debe permitir a los usuarios registrar nuevas prendas, dando información como nombre, tipo de prenda, color, talla, temporada (invierno, verano) y foto de la prenda, estado.
	Los usuarios deben poder editar la información de una prenda existente (modificar el estado, agregar nuevas fotos, cambiar la categoría).
	El sistema debe permitir eliminar una prenda de la lista.
	Los usuarios deben poder cambiar la categoría de una prenda (por ejemplo, pasar una prenda de "ropa de verano" a "ropa de invierno").
	El usuario podrá cambiar el estado de la prenda dependiendo que tan disponible o no(lista, lavando, arreglando, averiada)

3.	Combinación de Outfits:
	Los usuarios deben poder seleccionar varias prendas de su armario para crear un outfit.
	El sistema debe mostrar sugerencias de prendas complementarias al crear un outfit basado en el color, tipo de prenda y temporada.
	El sistema debe permitir al usuario visualizar el outfit completo y realizar cambios antes de guardarlo.
	Los outfits guardados deben ser modificables (agregar, quitar prendas) y eliminables por el usuario.
4.	Recomendaciones de Outfits:
	El sistema debe ofrecer recomendaciones diarias de outfits, basadas en la información dada por el usuario antes de comenzar a usar la aplicación por ejemplo sobre el clima, eventos programados.
	El sistema debe aprender de las preferencias del usuario mediante una caracterización del perfil que considere:
	Tipos de prendas más usadas.
	Colores preferidos.
	Estilos más seleccionados.
	Las recomendaciones deben adaptarse al estado de las prendas, evitando sugerir aquellas que hayan sido marcadas como "lavando", "sin usar", dependiendo el clima u ocasión.

6.	Búsqueda y Filtrado de Prendas:
	Los usuarios deben poder realizar búsquedas por palabras clave, como nombre de la prenda, tipo, color, categoría o estado (por ejemplo, "pantalón azul").
	El sistema debe permitir filtrar las prendas por categorías (camisas, pantalones, vestidos), colores, temporadas (verano, invierno).
	El sistema debe ofrecer una vista de lista o galería para visualizar las prendas filtradas, mostrando las fotos y los detalles de cada prenda.







Requisitos no funcionales:
1.	Rendimiento:
•	Tiempo de respuesta: el sistema debe cargar las recomendaciones de outfits y lista de prendas lo más rápido posible aprox no más de 3 seg
•	Capacidad: la aplicación debe poder gestionar la mayor cantidad (1000)de prendas por usuario sin afectar el rendimiento ni ponerlo lento 
•	Escalabilidad: El sistema debe ser capaz de soportar múltiples usuarios simultáneamente.
2.	Seguridad:
•	Autenticación: el sistema deberá rechazar todas las solicitudes nos acreditadas
3.	Usabilidad:
•	Interfaz de usuario intuitiva: la interfaz debe ser fácil de usar permitiendo que los usuarios tengan la mejor experiencia posible
•	Compatibilidad multiplataforma: se debe poder usar en cualquier tipo de dispositivo.
4.	Mantenibilidad:
•	Modularidad del código: el código debe estar diseñado de manera modular para que se puedan agregar nuevas categorías o funciones sin alterar otras partes del código
•	
5.	Fiabilidad:
•	Disponibilidad: el sistema debe estar disponible el 99.9% del tiempo para que las personas en cualquier momento puedan ver su closet virtual
6.	Escalabilidad:
•	Aumento progresivo de usuarios: el sistema deber permitir ir ingresando progresivamente cada vez mas usuarios si perder su rendimiento y eficacia
•	Gestión de grandes volúmenes de datos: debe poder soportar gran volumen de datos u imágenes optimizando el espacio
7.	Compatibilidad:
•	Integración de servicios externos: deberá aceptar servicios externos para integrar nuevas funcionalidades en el sistema
•	Actualizaciones automáticas: el sistema debe permitir actualizar el software sin interrumpir a los usuarios mientras navegan.


