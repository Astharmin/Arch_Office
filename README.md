# 🛠️ Autómata de Microsoft Office con Python

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wizardry-green.svg)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20Ninja-yellow.svg)
![Estado](https://img.shields.io/badge/Estado-Evolucionando%20🚀-orange.svg)

## ⚡ ¿Qué es Arch_Office?

Es tu asistente digital para tareas repetitivas de oficina. ¿Cansado de revisar a mano cientos de filas en Excel, de formatear documentos de Word uno por uno, o de enviar correos genéricos? Este conjunto de scripts en Python automatiza todo eso y más, liberándote para hacer un trabajo más creativo e interesante.

¡Deja que el código haga el trabajo pesado por ti!

## 🧩 Módulos y Funcionalidades

Este repositorio es un **toolkit modular**. Puedes usar cada script por separado para resolver un problema específico, o combinarlos para crear flujos de trabajo complejos.

| Módulo | Script | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **🧮 Validador de Excel** | `detective_notas.py` | Tu detective personal de hojas de cálculo. Encuentra errores, duplicados y datos faltantes en archivos Excel académicos. | ✅ **Activo** |
| **📝 Automatizador de Word** | *`word_mago.py`* | Genera y personaliza documentos de Word a partir de plantillas y datos variables. Ideal para informes, contratos o cartas masivas. | 🔜 **Próximamente** |
| **📧 Enviador de Correos** | *`mail_bot.py`* | Envía correos electrónicos personalizados en masa, con archivos adjuntos. Perfecto para notificaciones o boletines. | 🔜 **Próximamente** |

---

## 🔍 Spotlight: El Validador de Excel (`detective_notas.py`)

Esta herramienta ya está en funcionamiento y es un claro ejemplo del poder de la automatización. Escanea archivos Excel de notas y te alerta sobre inconsistencias que un vistazo humano podría pasar por alto.

### ⚠️ Lo que Detecta:
*   **Notas Imposibles**: ¿Matemáticas: 17.5? ¡Rompe la escala!
*   **Asignaturas Fantasma**: ¿A un alumno le falta Inglés? Sospechoso.
*   **Clones Académicos**: ¿3 veces Educación Física? ¡Error de copiar-pegar!

### 🎯 Uso Rápido:
```bash
python detective_notas.py
```
**Salida de ejemplo:**
```
============================================================
SISTEMA DE VALIDACIÓN DE NOTAS ACADÉMICAS
============================================================
📊 Datos cargados: 150 registros
⚠ Luis - Tecnología: Nota T1 = 25 (¡Fuera de rango!)
⚠ Ana tiene la asignatura 'Inglés' duplicada (3 veces)
✅ Validación completada. Se encontraron 2 tipos de errores.
```

> **💡 Esta es solo la punta del iceberg.** El mismo principio de leer, analizar y actuar sobre datos de Office se aplica a los módulos de Word y Correo que están en camino.

---

## 🏗️ Estructura del Proyecto (Evolutiva)

```
Arch_Office/
│
├── 📁 SRC/                           # Recursos y datos de ejemplo
│   └── Notas_Alumnos.xlsx
│
├── 🧮 detective_notas.py             # Módulo 1: Validador de Excel (LISTO)
├── 📝 word_mago.py                   # Módulo 2: Automatizador de Word (PRÓXIMO)
├── 📧 mail_bot.py                    # Módulo 3: Enviador de Correos (PRÓXIMO)
│
├── 📋 README.md                      # Esta documentación
├── 📜 requirements.txt               # Dependencias del proyecto
└── ⚖️ LICENSE                        # Licencia MIT
```

---

## 🚀 Cómo Empezar

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Astharmin/Arch_Office.git
    cd Arch_Office
    ```

2.  **Configura tu entorno (recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(El archivo `requirements.txt` debe incluir `pandas`, `openpyxl` y en el futuro librerías para Word y email)*

4.  **¡Ejecuta y automatiza!**
    ```bash
    # Prueba el validador de Excel
    python detective_notas.py
    ```

---

## 📅 Hoja de Ruta (Roadmap)

El proyecto está vivo y en constante evolución. Este es el plan:

*   **✅ Fase 1: Cimientos (Completado)**
    *   Validador robusto de archivos Excel (`detective_notas.py`).
*   **🔨 Fase 2: Expansión (En Progreso)**
    *   Desarrollo del módulo `word_mago.py` para generar documentos.
    *   Desarrollo del módulo `mail_bot.py` para envío de correos.
*   **🔮 Fase 3: Integración y Potencia (Futuro)**
    *   Crear un script `orquestador.py` que combine varios módulos en un flujo de trabajo.
    *   Añadir una interfaz de línea de comandos (CLI) más amigable.
    *   Soporte para más formatos (PDF, PowerPoint).

**¿Tienes una idea para un nuevo módulo o una mejora?** ¡Tu contribución es bienvenida! Revisa la sección de contribuciones.

---

## 🤝 ¿Quieres Contribuir?

¡Me encantaría que este toolkit creciera con la ayuda de la comunidad! Puedes ayudar de varias formas:

1.  **🐛 Reportar un Bug:** ¿Encontraste un error? Ábreme un *issue*.
2.  **💡 Sugerir una Mejora:** ¿Tienes una idea para un nuevo módulo o funcionalidad? ¡Hablemos!
3.  **🔧 Enviar un Pull Request (PR):** Si implementaste una corrección o una nueva característica, envíala.
4.  **📚 Mejorar la Documentación:** ¿Encontraste algo poco claro en este README? Tu ayuda para hacerlo más comprensible es invaluable.

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. En resumen: puedes usar, modificar y distribuir este código libremente, incluso con fines comerciales. Solo se pide atribución. Para más detalles, consulta el archivo `LICENSE`.

## ✨ Autor

- **Astharmin** -
> "La tecnología debería liberarnos del trabajo repetitivo, no crearlo."

---

⭐ **¿Te parece útil automatizar tareas de oficina? ¡Dale una estrella al repositorio para apoyar su desarrollo!** ⭐
