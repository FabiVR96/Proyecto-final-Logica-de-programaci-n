 
PROYECTO INTEGRADOR

Nombre: Fabian Villanueva Ross
Curso: Logica de programacion 1-sof-1c
Profesor: Monica Patricia Salazar Tapia

Índice

1. Introducción
2. Descripción del problema
3. Justificación
4. Objetivos
    4.1 Objetivo general
    4.2 Objetivos específicos
5. Planificación del proyecto
   5.1 Alcance del sistema
   5.2 Problema que se desea resolver
   5.3 Cronograma de actividades 
6. Diseño del sistema
   6.1 Diagrama de Casos de Uso
   6.2 Diagrama de Flujo
   6.3 Diagrama de Arquitectura
   6.4 Descripción de los diagramas





7. Desarrollo del software
   7.1 Herramientas utilizadas
   7.2 Configuración del entorno de desarrollo
   7.3 Descripción del código
   7.4 Funcionalidades implementadas
   7.5 Estructuras condicionales
   7.6 Estructuras repetitivas
   7.7 Organización del código
   7.8 Uso de GitHub
8. Relación con los contenidos de la asignatura
9. Impacto de las nuevas tecnologías en la sociedad
10. Reflexión personal
11. Conclusiones
12. Bibliografía

1.- Introducción

En la actualidad, el desarrollo de software desempeña un papel fundamental en la transformación de la sociedad, ya que permite automatizar procesos, facilitar la comunicación, optimizar la toma de decisiones y ofrecer soluciones tecnológicas para diferentes necesidades. El avance constante de las nuevas tecnologías ha impulsado la creación de aplicaciones capaces de resolver problemas de manera eficiente, convirtiendo a la programación en una de las habilidades más importantes dentro del ámbito académico y profesional.
El presente proyecto integrador tiene como finalidad aplicar de manera práctica los conocimientos adquiridos durante el curso mediante el desarrollo de una aplicación informática basada en el juego Piedra, Papel o Tijera. Aunque se trata de un juego sencillo y ampliamente conocido, su implementación representa una excelente oportunidad para integrar conceptos fundamentales del desarrollo de software, desde el análisis del problema hasta la programación, las pruebas y la documentación del sistema
El desarrollo del proyecto inició con la identificación del problema y la definición del alcance del sistema. Posteriormente, se realizó el diseño mediante diagramas de casos de uso, diagramas de flujo y un diagrama de arquitectura, herramientas que permitieron representar gráficamente las funcionalidades del programa, la interacción entre el usuario y el sistema, y la organización de los componentes principales antes de comenzar la etapa de programación. Esta fase de planificación facilitó la comprensión del funcionamiento del software y sirvió como guía durante todo el proceso de desarrollo.

La implementación del sistema se llevó a cabo utilizando el lenguaje de programación Python, debido a su sintaxis clara y facilidad para el aprendizaje de la programación estructurada. Durante el desarrollo se aplicaron diversos conceptos estudiados en la asignatura, tales como el uso de variables para almacenar información, listas para organizar las opciones del juego, estructuras condicionales para evaluar las reglas de cada partida, estructuras repetitivas para permitir múltiples rondas, funciones para modularizar el código y mejorar su reutilización, así como la biblioteca “random” para generar de forma aleatoria la elección de la computadora. Asimismo, se incorporaron comentarios dentro del código con el propósito de facilitar su comprensión y mantenimiento.
Además de los conceptos básicos de programación, el proyecto también integra herramientas utilizadas en el desarrollo profesional de software. Se empleó Visual Studio Code como entorno de desarrollo integrado y GitHub como sistema de control de versiones, permitiendo organizar el código fuente, registrar el progreso del proyecto y mantener una copia segura del trabajo realizado. Estas herramientas representan prácticas comunes dentro de la industria del desarrollo de software y fortalecen las competencias del estudiante para futuros proyectos.
Por otra parte, el desarrollo de esta aplicación permite reflexionar sobre el impacto de las nuevas tecnologías en la sociedad. Actualmente, el software está presente en prácticamente todas las actividades cotidianas, desde aplicaciones móviles y plataformas educativas hasta sistemas empresariales e inteligencia artificial. Incluso programas sencillos como el desarrollado en este proyecto evidencian cómo la programación puede utilizarse para crear soluciones funcionales, mejorar la experiencia de los usuarios y servir como base para aplicaciones de mayor complejidad.
Finalmente, este documento presenta el proceso completo de desarrollo del proyecto, incluyendo la planificación, el análisis del problema, el diseño del sistema, la implementación del código, la utilización de herramientas de desarrollo, la integración de los contenidos estudiados durante el curso y una reflexión sobre la importancia que tienen las nuevas tecnologías en la sociedad actual. De esta manera, el proyecto no solo demuestra el funcionamiento de una aplicación informática, sino también el aprendizaje adquirido durante la asignatura y la capacidad para aplicar dichos conocimientos en la construcción de una solución tecnológica funcional.



2.- Descripción del problema

El avance de las nuevas tecnologías ha transformado la forma en que las personas aprenden, trabajan, se comunican y se entretienen. Actualmente, el desarrollo de software permite automatizar procesos, facilitar la interacción entre usuarios y sistemas, y ofrecer soluciones innovadoras para una gran variedad de necesidades. En este contexto, la programación se ha convertido en una herramienta fundamental para crear aplicaciones capaces de resolver problemas de manera eficiente y mejorar la experiencia de los usuarios.
En este proyecto se plantea el desarrollo de una aplicación informática basada en el juego Piedra, Papel o Tijera, cuyo propósito es permitir que un usuario juegue contra la computadora de forma interactiva. Aunque se trata de un juego sencillo, su implementación implica resolver diversos problemas relacionados con la lógica de programación, la validación de datos, la interacción con el usuario y la organización del software.
El sistema debe ser capaz de recibir correctamente la elección del jugador, generar una decisión aleatoria para la computadora, comparar ambas jugadas aplicando las reglas del juego y determinar el resultado de cada partida. Además, el programa debe ofrecer funcionalidades adicionales como un menú principal, registro de estadísticas, almacenamiento de datos en archivos y un historial de partidas, proporcionando una experiencia más completa para el usuario.
Desde el punto de vista académico, el desarrollo de este proyecto representa una oportunidad para integrar los contenidos estudiados durante la asignatura, aplicando conceptos de análisis de problemas, diseño de software, programación estructurada y uso de herramientas de desarrollo. Asimismo, permite comprender cómo incluso aplicaciones sencillas requieren una planificación adecuada, una arquitectura organizada y una implementación correcta para garantizar su funcionamiento.










3.- Justificación

El desarrollo de este proyecto se justifica por la necesidad de aplicar de forma práctica los conocimientos adquiridos durante la asignatura de programación y desarrollo de software. A través de la construcción de una aplicación funcional, el estudiante tiene la oportunidad de fortalecer habilidades relacionadas con el análisis de problemas, el diseño de soluciones y la implementación de programas utilizando un lenguaje de programación moderno como Python.
La elección del juego Piedra, Papel o Tijera permite desarrollar un sistema de complejidad moderada que integra diferentes conceptos fundamentales de la programación, tales como el uso de variables, listas, tuplas, diccionarios, funciones, estructuras condicionales, estructuras repetitivas, manejo de archivos y generación de datos aleatorios mediante bibliotecas del lenguaje. Además, el proyecto promueve la aplicación de buenas prácticas de desarrollo, como la organización modular del código, la documentación mediante comentarios y el uso de GitHub como herramienta de control de versiones.
Por otra parte, este proyecto evidencia la importancia que tienen las nuevas tecnologías en la sociedad actual. El desarrollo de software constituye una de las principales herramientas para crear soluciones que facilitan las actividades cotidianas, mejoran los procesos de aprendizaje, impulsan la innovación y contribuyen al avance tecnológico en diferentes sectores. Aunque el sistema desarrollado corresponde a un juego, las metodologías y técnicas utilizadas son las mismas que se emplean en aplicaciones de mayor escala, lo que convierte este proyecto en una base sólida para futuros desarrollos más complejos.
Finalmente, este trabajo no solo tiene como objetivo cumplir con los requisitos académicos de la asignatura, sino también fortalecer competencias técnicas y profesionales que serán de gran utilidad en la formación como desarrollador de software, fomentando el pensamiento lógico, la resolución de problemas y el uso de herramientas ampliamente utilizadas en la industria tecnológica.








4.- Objetivos

Objetivo General

Desarrollar una aplicación informática del juego Piedra, Papel o Tijera utilizando el lenguaje de programación Python, aplicando los conocimientos adquiridos durante la asignatura sobre análisis de problemas, diseño de software, programación estructurada, organización del código y uso de herramientas de desarrollo, con el fin de demostrar la integración de los contenidos estudiados y reflexionar sobre el impacto de las nuevas tecnologías en la sociedad.

Objetivos Específicos

A) Analizar una problemática y definir el alcance del sistema antes de iniciar su desarrollo.
B) Diseñar diagramas de casos de uso, diagramas de flujo y arquitectura de software para representar las funcionalidades y la estructura del sistema.
C) Implementar un programa funcional utilizando Python, aplicando estructuras condicionales, estructuras repetitivas y funciones para organizar el código de manera clara y modular.
D) Utilizar listas para almacenar y gestionar las opciones del juego, así como la biblioteca random para generar decisiones aleatorias de la computadora.
E) Incorporar comentarios y buenas prácticas de programación que faciliten la comprensión, el mantenimiento y la reutilización del código.
F) Emplear GitHub como herramienta de control de versiones para almacenar y gestionar el desarrollo del proyecto de manera organizada.
G) Documentar el proceso de desarrollo mediante un informe técnico que incluya el análisis del problema, los diagramas, la explicación del sistema y las conclusiones obtenidas.
H) Reflexionar sobre la importancia del desarrollo de software y el impacto que tienen las nuevas tecnologías en la sociedad, destacando cómo la programación contribuye a la creación de soluciones para diferentes necesidades.



5.- Planificación del Proyecto

5.1 Alcance del sistema
El presente proyecto tiene como alcance el desarrollo de una aplicación informática denominada Piedra, Papel o Tijera Plus, implementada en el lenguaje de programación Python. El sistema permitirá que un usuario juegue contra la computadora mediante una interfaz de consola sencilla e intuitiva, aplicando las reglas tradicionales del juego.
El programa contará con un menú principal desde el cual el usuario podrá iniciar una nueva partida, consultar las estadísticas acumuladas, reiniciar el marcador, visualizar información sobre la aplicación y salir del sistema. Asimismo, el software registrará las victorias, derrotas y empates obtenidos durante la sesión de juego, permitiendo además almacenar esta información en archivos para conservar los datos entre diferentes ejecuciones del programa.
Durante el desarrollo se aplicarán conceptos fundamentales de programación, como el uso de variables, listas, tuplas, diccionarios, funciones, estructuras condicionales, estructuras repetitivas y manejo de archivos. Además, el proyecto utilizará GitHub como herramienta de control de versiones y Visual Studio Code como entorno de desarrollo, siguiendo buenas prácticas de organización y documentación del código.
Aunque el sistema será desarrollado como una aplicación de consola, su diseño modular permitirá que en futuras versiones pueda ampliarse fácilmente mediante la incorporación de una interfaz gráfica, nuevos modos de juego, niveles de dificultad, ranking de jugadores o almacenamiento en bases de datos.

5.2 Problema que se desea resolver

El proyecto busca desarrollar una aplicación que permita a un usuario jugar Piedra, Papel o Tijera contra la computadora de forma automática e interactiva. Para ello, el sistema deberá generar decisiones aleatorias, aplicar correctamente las reglas del juego y proporcionar retroalimentación inmediata sobre el resultado de cada partida.
Además del funcionamiento básico del juego, se pretende ofrecer una mejor experiencia de usuario mediante la incorporación de un menú principal, almacenamiento de estadísticas, historial de partidas y una estructura de código organizada que facilite el mantenimiento y futuras mejoras del sistema.
Desde el punto de vista académico, este proyecto también busca integrar los conocimientos adquiridos durante la asignatura, demostrando la aplicación de metodologías de análisis, diseño y desarrollo de software en una solución funcional.
5.3 Cronograma de actividades

Semana	Actividad	Resultado esperado
1	Análisis del problema y definición del alcance del sistema.	Identificación del problema, objetivos y planificación inicial.
2	Investigación sobre diagramas UML y arquitectura de software. Elaboración de diagramas de casos de uso, flujo y arquitectura.	Diseño funcional y estructural del sistema.
3	Configuración del entorno de desarrollo (Python, Visual Studio Code y GitHub). Creación del repositorio del proyecto.	Entorno de trabajo preparado y repositorio configurado.
4	Desarrollo de la estructura principal del programa y del menú de navegación.	Primera versión funcional del sistema.
5	Implementación de la lógica del juego utilizando funciones, listas, tuplas, diccionarios, estructuras condicionales y repetitivas.	Juego completamente funcional.
6	Desarrollo del módulo de estadísticas, historial de partidas y almacenamiento de datos mediante archivos de texto.	Funcionalidades adicionales implementadas y probadas.
7	Pruebas del sistema, corrección de errores, optimización del código y actualización de la documentación del proyecto.	Sistema estable y documentación completa.
8	Elaboración del informe final, preparación del video de presentación y entrega del proyecto integrador.	Proyecto finalizado y listo para su evaluación.

 
6.- Diseño del sistema

El diseño del sistema constituye una etapa fundamental dentro del desarrollo del software, ya que permite representar de forma gráfica las funcionalidades del programa, la interacción entre el usuario y el sistema, así como la estructura general de los componentes que conforman la aplicación. Mediante el uso de diagramas es posible comprender el funcionamiento del software antes de iniciar la implementación del código, facilitando la organización del proyecto y reduciendo la posibilidad de errores durante el desarrollo.
Para el presente proyecto se utilizaron tres tipos de diagramas: el diagrama de casos de uso, el diagrama de flujo y el diagrama de arquitectura, los cuales describen las funcionalidades principales del sistema, el proceso lógico del juego y la organización de sus componentes internos.

6.1 Diagrama de Casos de Uso

El diagrama de casos de uso representa las diferentes acciones que el usuario puede realizar dentro del sistema y las funcionalidades que ofrece el programa. En este proyecto existe un único actor principal, el usuario, quien interactúa con el sistema mediante un menú que permite acceder a todas las opciones disponibles.
 
6.2 Diagrama de Flujo

El diagrama de flujo representa la secuencia lógica que sigue el programa desde que el usuario inicia la aplicación hasta que decide finalizarla.
 
6.3 Diagrama de Arquitectura
La arquitectura del sistema representa la organización de los diferentes módulos que conforman el programa y la relación existente entre ellos.

 

6.4 Relación entre los diagramas y el sistema

Los diagramas elaborados representan de forma clara el funcionamiento general del programa y sirven como guía durante el desarrollo del software. El diagrama de casos de uso identifica las funcionalidades que ofrece el sistema al usuario; el diagrama de flujo describe el proceso lógico que sigue cada partida; y el diagrama de arquitectura muestra la organización interna de los módulos que conforman la aplicación.
Gracias a este diseño previo fue posible desarrollar un sistema estructurado, modular y fácil de mantener, facilitando tanto la implementación del código como futuras mejoras del proyecto.




7.- Desarrollo del Software

El desarrollo del software corresponde a la etapa en la que el diseño previamente elaborado fue transformado en una aplicación funcional mediante el lenguaje de programación Python. Durante esta fase se implementaron las funcionalidades definidas en los diagramas, procurando mantener una estructura organizada, modular y fácil de mantener
Para el desarrollo del proyecto se aplicaron diversos conceptos estudiados durante la asignatura, tales como programación estructurada, funciones, listas, tuplas, diccionarios, estructuras condicionales, estructuras repetitivas y manejo de archivos. Asimismo, se empleó GitHub como herramienta de control de versiones para registrar el progreso del proyecto y facilitar la administración del código fuente.
El objetivo principal durante esta etapa fue construir una aplicación que no solo cumpliera con los requisitos funcionales del juego, sino que también siguiera buenas prácticas de programación y organización del software.

7.1 Herramientas utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:
Herramienta	Descripción
Python 3	Lenguaje de programación utilizado para desarrollar la aplicación.
Visual Studio Code	Entorno de desarrollo integrado (IDE) empleado para escribir, ejecutar y depurar el código.
GitHub	Plataforma utilizada para almacenar el repositorio del proyecto y gestionar las versiones del código.

Estas herramientas permitieron desarrollar el sistema de forma organizada y siguiendo prácticas ampliamente utilizadas en el desarrollo profesional de software.





7.2 Configuración del entorno de desarrollo

Antes de iniciar la implementación del sistema se preparó el entorno de trabajo instalando Python y Visual Studio Code. Posteriormente se configuró Git para el control de versiones y se creó un repositorio en GitHub donde se almacenó todo el proyecto.
La estructura inicial del proyecto se organizó mediante diferentes archivos y carpetas, separando la lógica del juego, las estadísticas, las funciones auxiliares, la documentación y los diagramas. Esta organización facilita el mantenimiento del software y permite futuras ampliaciones sin afectar el funcionamiento general del programa.

7.3 Descripción del código

El código del programa fue desarrollado siguiendo una estructura modular, dividiendo las diferentes responsabilidades del sistema en archivos independientes.
El archivo main.py actúa como punto de entrada del programa, mostrando el menú principal y coordinando la interacción entre los diferentes módulos.
El archivo juego.py contiene la lógica principal del juego, incluyendo la obtención de las jugadas, la generación aleatoria de la elección de la computadora y la determinación del ganador de cada ronda.
El archivo estadisticas.py administra el registro de victorias, derrotas y empates, además de almacenar esta información en archivos para conservar el progreso del jugador.
Por último, utilidades.py reúne funciones auxiliares reutilizadas por diferentes módulos del programa, favoreciendo una mejor organización del código y evitando la duplicación de instrucciones.

7.4 Funcionalidades implementadas

El sistema desarrollado incorpora las siguientes funcionalidades:

Registro del nombre del jugador.
Menú principal interactivo.
Inicio de nuevas partidas.
Selección de piedra, papel o tijera.
Generación aleatoria de la jugada de la computadora.
Comparación automática de las jugadas.
Determinación del ganador.
Visualización del resultado de cada ronda.
Registro de victorias, derrotas y empates.
Almacenamiento permanente de estadísticas.
Historial de partidas.
Reinicio del marcador.
Salida segura del programa.
Estas funcionalidades cumplen con los requisitos planteados durante el análisis del problema y permiten ofrecer una experiencia de usuario más completa que la versión inicial del proyecto.

7.5 Aplicación de estructuras lógicas

Durante el desarrollo del programa se aplicaron diferentes estructuras de programación estudiadas en la asignatura.
Variables
	Se utilizaron para almacenar información temporal como el nombre del jugador, la jugada seleccionada, el resultado de cada partida y los datos estadísticos
Listas
	Se emplearon para almacenar las opciones disponibles del juego
Piedra
Papel
Tijera
También se utilizaron para gestionar el historial de partidas cuando fue necesario.

Tuplas
	Las reglas del juego fueron almacenadas mediante tuplas debido a que representan información fija que no cambia durante la ejecución del programa.

Diccionarios
	Las estadísticas del jugador fueron organizadas utilizando un diccionario que almacena las victorias, derrotas y empates mediante claves descriptivas.


Condicionales
	Las estructuras if, elif y else permitieron comparar las jugadas del usuario y la computadora para determinar el resultado de cada partida.

Estructuras repetitivas
	Se utilizó un bucle while para mantener el programa en ejecución hasta que el usuario decidiera salir del sistema.

Funciones
	El programa fue dividido en funciones específicas para facilitar la reutilización del código, mejorar la organización y hacer más sencilla la depuración del sistema.

Manejo de archivos
	Se implementó el uso de archivos de texto para almacenar de forma permanente las estadísticas y el historial de partidas, permitiendo conservar la información incluso después de cerrar el programa.


7.6 Organización del código
Con el propósito de facilitar el mantenimiento y futuras mejoras, el proyecto fue organizado en módulos independientes.
 
 
 
 
 





7.7 Uso de GitHub

Durante el desarrollo del proyecto se utilizó GitHub como plataforma para el control de versiones del código fuente.
El repositorio permitió registrar los cambios realizados en cada etapa del desarrollo, mantener una copia de seguridad del proyecto y organizar adecuadamente los archivos correspondientes a la documentación, diagramas y código fuente.
El uso de GitHub constituye una práctica ampliamente utilizada en el desarrollo profesional de software, ya que facilita el trabajo colaborativo, el seguimiento de cambios y la administración de proyectos informáticos.


 
 
7.8 Buenas prácticas aplicadas

Durante el desarrollo del software se aplicaron diversas buenas prácticas de programación con el objetivo de mejorar la calidad del código y facilitar su mantenimiento. Entre ellas se destacan:

Organización modular del proyecto.
Uso de nombres descriptivos para variables y funciones.
Separación de responsabilidades entre los diferentes archivos.
Inclusión de comentarios explicativos en las secciones más importantes del código.
Reutilización de funciones para evitar la duplicación de instrucciones.
Validación de las entradas del usuario para prevenir errores.
Almacenamiento organizado de la información en archivos.
Uso de GitHub para el control de versiones y respaldo del proyecto.
La aplicación de estas prácticas permitió desarrollar un software más ordenado, legible y preparado para futuras mejoras o ampliaciones.





8.- Relación con los contenidos de la asignatura

El desarrollo de este proyecto permitió integrar los principales contenidos estudiados durante la asignatura, aplicando tanto conceptos teóricos como habilidades prácticas relacionadas con el análisis, diseño e implementación de software. En la primera etapa se realizó el análisis del problema y la definición del alcance del sistema, permitiendo comprender las necesidades del usuario antes de iniciar el desarrollo. Posteriormente, se elaboraron diagramas de casos de uso, diagramas de flujo y un diagrama de arquitectura, aplicando técnicas de modelado para representar gráficamente el funcionamiento del sistema y la relación entre sus componentes.
Durante la implementación se utilizaron conceptos fundamentales de programación estructurada mediante el lenguaje Python. Se aplicaron variables para almacenar información, listas para organizar datos, tuplas para representar reglas fijas del juego, diccionarios para gestionar las estadísticas del usuario, funciones para modularizar el código y estructuras condicionales y repetitivas para controlar la lógica del programa. Además, se incorporó el manejo de archivos para conservar las estadísticas y el historial de partidas entre diferentes ejecuciones del sistema.
El proyecto también permitió utilizar herramientas propias del desarrollo profesional de software, como Visual Studio Code para la programación y GitHub para el control de versiones y la gestión del repositorio. Estas herramientas facilitaron la organización del proyecto y permitieron documentar adecuadamente el proceso de desarrollo.
En conjunto, este proyecto representa la integración de los conocimientos adquiridos durante las diferentes unidades de la asignatura, demostrando la capacidad para desarrollar una aplicación funcional siguiendo un proceso ordenado de análisis, diseño, programación y documentación.

9.- Impacto de las nuevas tecnologías en la sociedad

Las nuevas tecnologías han transformado profundamente la manera en que las personas viven, trabajan, estudian y se comunican. Actualmente, el desarrollo de software está presente en prácticamente todos los sectores de la sociedad, permitiendo automatizar procesos, optimizar recursos y ofrecer soluciones que facilitan las actividades cotidianas.
En el ámbito educativo, la tecnología ha permitido crear plataformas de aprendizaje, simuladores, videojuegos educativos y aplicaciones interactivas que favorecen el desarrollo de nuevas habilidades. En el sector empresarial, los sistemas informáticos mejoran la gestión de la información, aumentan la productividad y facilitan la toma de decisiones. Asimismo, en áreas como la salud, el transporte, la banca y la comunicación, el software desempeña un papel fundamental en la prestación de servicios más eficientes y seguros.
Aunque el proyecto desarrollado corresponde a un juego, su construcción demuestra cómo los principios utilizados para desarrollar aplicaciones sencillas son los mismos que se emplean en sistemas de mayor complejidad. Conceptos como el análisis de problemas, el diseño de software, la programación modular, el control de versiones y la documentación forman parte de cualquier proyecto tecnológico moderno.
Además, el avance de tecnologías como la inteligencia artificial, la computación en la nube, el Internet de las Cosas (IoT) y el análisis de datos está generando nuevas oportunidades para el desarrollo de soluciones innovadoras que respondan a las necesidades de la sociedad. Por ello, adquirir conocimientos de programación y desarrollo de software representa una competencia cada vez más valiosa para afrontar los retos tecnológicos del futuro. En este contexto, proyectos como el desarrollado en esta asignatura constituyen una base importante para comprender cómo la tecnología puede utilizarse para resolver problemas reales y contribuir al desarrollo de nuevas soluciones informáticas.

10.- Reflexión personal

El desarrollo de este proyecto representó una experiencia enriquecedora que me permitió poner en práctica los conocimientos adquiridos durante la asignatura y comprender de una manera más clara el proceso completo de creación de un software. A lo largo del proyecto aprendí que desarrollar una aplicación no consiste únicamente en escribir código, sino también en analizar el problema, planificar la solución, diseñar el sistema, organizar adecuadamente el proyecto y documentar cada etapa del proceso.
Uno de los aspectos que considero más importantes fue la utilización de herramientas como GitHub para el control de versiones y la organización del código mediante módulos y funciones. Estas prácticas me permitieron comprender la importancia de mantener un proyecto ordenado y preparado para futuras mejoras, tal como ocurre en el desarrollo profesional de software. También fortalecí mis habilidades en el lenguaje Python, aplicando estructuras condicionales, estructuras repetitivas, funciones, listas, tuplas, diccionarios y manejo de archivos para construir una aplicación funcional y organizada. Cada uno de estos conceptos aportó una mejor comprensión sobre la lógica de programación y la forma en que diferentes componentes pueden trabajar conjuntamente para resolver un problema.
Finalmente, este proyecto incrementó mi interés por continuar aprendiendo sobre desarrollo de software y nuevas tecnologías. Considero que los conocimientos adquiridos durante esta asignatura constituyen una base sólida para enfrentar proyectos de mayor complejidad y seguir desarrollando habilidades que serán de gran utilidad en mi formación académica y profesional.

11.- Conclusiones

El desarrollo del proyecto permitió integrar de manera práctica los conocimientos adquiridos durante la asignatura, siguiendo las diferentes etapas del proceso de desarrollo de software: análisis del problema, planificación, diseño, implementación, pruebas y documentación. Gracias a este enfoque fue posible construir una aplicación funcional que cumple con los objetivos planteados y responde a la problemática identificada.
Durante la implementación se aplicaron conceptos fundamentales de programación como variables, listas, tuplas, diccionarios, funciones, estructuras condicionales, estructuras repetitivas y manejo de archivos, demostrando la importancia de estos elementos para construir programas organizados, reutilizables y fáciles de mantener. Asimismo, la utilización de GitHub permitió comprender la utilidad del control de versiones y la organización profesional del código fuente. El proyecto también evidenció la importancia del diseño previo mediante diagramas de casos de uso, flujo y arquitectura, ya que estos facilitaron la comprensión del funcionamiento del sistema antes de iniciar la programación y sirvieron como guía durante todo el proceso de desarrollo.
Finalmente, este trabajo permitió reflexionar sobre el impacto que tienen las nuevas tecnologías en la sociedad y sobre el papel que desempeña el desarrollo de software en la creación de soluciones para diferentes necesidades. Aunque el sistema desarrollado corresponde a un juego, las metodologías, herramientas y buenas prácticas aplicadas son las mismas que se utilizan en proyectos de mayor escala, convirtiendo esta experiencia en una base importante para futuros desarrollos y fortaleciendo las competencias necesarias para continuar formándome como desarrollador de software.

12.- Bibliografía

Python Software Foundation. (2026). Python Documentation. https://docs.python.org/3/
GitHub. (2026). GitHub Documentation. https://docs.github.com/
Visual Paradigm. (2026). UML Use Case Diagram Tutorial. https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/
Microsoft. (2026). Visual Studio Code Documentation. https://code.visualstudio.com/docs
