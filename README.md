# 🛠️ Arch_Office: Automatización Inteligente de Microsoft Office con Python

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wizardry-green.svg)
![python-docx](https://img.shields.io/badge/python--docx-Word%20Automation-blue.svg)
![Estado](https://img.shields.io/badge/Estado-En%20Expansión%20🚀-orange.svg)

## ⚡ ¿Qué es Arch_Office?

**Arch_Office** es tu asistente digital para tareas repetitivas de oficina. Este toolkit en Python transforma horas de trabajo manual en segundos de procesamiento automático, liberándote para tareas más creativas y estratégicas.

¿Cansado de revisar hojas de cálculo, generar documentos uno por uno o enviar correos masivos? ¡Deja que el código haga el trabajo pesado!

## 🎯 Avances Recientes: ¡Word_Mago está Vivo! ✨

**¡Gran noticia!** El módulo `word_mago.py` ya está operativo y listo para usar. Ahora puedes generar documentos de Word personalizados automáticamente a partir de datos de Excel, completando así un flujo de trabajo integral.

### 🔄 Flujo de Trabajo Completo:
```
Excel (Datos) → Detective_Notas (Validación) → Word_Mago (Generación) → OUTPUT (Documentos listos)
```

---

## 🧩 Módulos y Funcionalidades Actualizadas

| Módulo | Script | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **🔍 Validador de Excel** | `detective_notas.py` | Tu detective personal que encuentra errores, duplicados y datos faltantes en Excel. | ✅ **Activo** |
| **✨ Generador de Word** | `word_mago.py` | **¡NUEVO!** Crea documentos Word personalizados a partir de plantillas y datos de Excel. Genera informes de notas con promedios y clasificaciones automáticas. | ✅ **Activo** |
| **📧 Enviador de Correos** | `mail_bot.py` | Próximamente: Envío masivo de correos personalizados con adjuntos. | 🔜 **En Desarrollo** |

---

## ✨ Spotlight: Word_Mago en Acción

### 🎩 ¿Qué hace este mago?
1. **Lee datos combinados** de múltiples hojas de Excel
2. **Calcula automáticamente** promedios y clasificaciones (REPROBADO, APROBADO, EXIMIDO, SOBRESALIENTE)
3. **Genera documentos individuales** para cada alumno
4. **Aplica colores diferenciados** según la calificación
5. **Organiza la salida** en carpetas limpias con nombres normalizados

### 🎨 Características Principales:
- **Personalización total**: Cada documento incluye nombre del alumno, clase y curso
- **Cálculos automáticos**: Promedios de tres trimestres con clasificación por color
- **Manejo robusto**: Eliminación de tildes en nombres de archivo, gestión de errores
- **Resumen detallado**: Genera reporte de proceso con éxitos y fallos

### 🚀 Uso Rápido:
```bash
python word_mago.py
```

**Salida de ejemplo:**
```
============================================================
GENERADOR DE DOCUMENTOS DE NOTAS
============================================================
Directorio listo: .\OUTPUT
Datos de notas cargados: 300 registros
Datos de alumnos cargados: 25 registros
Datos combinados: 300 registros

Procesando 25 alumnos...
--------------------------------------------------
[  1/25] ✅ Juan Pérez
[  2/25] ✅ María González
[  3/25] ✅ Carlos Rodríguez
...
[ 25/25] ✅ Ana López

============================================================
RESUMEN DEL PROCESO
============================================================
Total alumnos procesados: 25
Documentos generados: 25
Errores: 0

✅ Proceso completado!
```

### 📁 Estructura de Salida:
```
OUTPUT/
├── NOTAS_JUAN_PEREZ.docx
├── NOTAS_MARIA_GONZALEZ.docx
├── NOTAS_CARLOS_RODRIGUEZ.docx
├── ...
└── resumen_proceso.txt
```

---

## 🏗️ Estructura del Proyecto Actualizada

```
Arch_Office/
│
├── 📁 SRC/                           # Recursos y plantillas
│   ├── Notas_Alumnos.xlsx           # Datos de ejemplo (hojas: Notas, Datos_Alumnos)
│   └── Plantilla_Final.docx          # Plantilla Word para documentos
│
├── 📁 OUTPUT/                        # Documentos generados (se crea automáticamente)
│
├── 🔍 detective_notas.py             # Módulo 1: Validador de Excel ✅
├── ✨ word_mago.py                   # Módulo 2: Generador de Word ✅ (¡NUEVO!)
├── 📧 mail_bot.py                    # Módulo 3: Enviador de Correos 🔜
│
├── 📋 README.md                      # Esta documentación
├── 📜 requirements.txt               # Dependencias del proyecto
└── ⚖️ LICENSE                        # Licencia MIT
```

---

## 🔧 Configuración y Uso

### 1. Instalación de Dependencias
```bash
# Asegúrate de tener las librerías necesarias
pip install pandas openpyxl python-docx
```

### 2. Preparar Archivos de Entrada
- **Excel**: Debe contener al menos dos hojas: `Notas` y `Datos_Alumnos`
- **Plantilla Word**: Documento con marcadores de posición para los datos

### 3. Ejecutar los Módulos
```bash
# Primero valida tus datos
python detective_notas.py

# Luego genera los documentos
python word_mago.py

# Próximamente: enviar por correo
# python mail_bot.py
```

---

## 📊 Roadmap Actualizado

### ✅ **Fase 1: Cimientos Sólidos (Completada)**
- Validador robusto de archivos Excel (`detective_notas.py`)
- Sistema de generación de documentos Word (`word_mago.py`)

### 🔨 **Fase 2: Integración de Comunicación (En Progreso)**
- Desarrollo del módulo `mail_bot.py` para envío automático de correos
- Conexión entre generación de documentos y envío

### 🔮 **Fase 3: Suite Completa (Próximo)**
- Script `orquestador.py` que ejecute el flujo completo (validar → generar → enviar)
- Interfaz de línea de comandos (CLI) más amigable
- Soporte para más formatos (PDF, PowerPoint)
- Dashboard web para monitoreo de procesos

---

## 🎯 Casos de Uso Real

### 📚 Para Instituciones Educativas:
- Generar boletines de notas personalizados para todos los alumnos
- Validar consistencia de datos antes de publicar calificaciones
- Enviar informes a padres y tutores automáticamente

### 🏢 Para Empresas:
- Generar informes de desempeño individuales
- Crear contratos o documentos personalizados
- Automatizar comunicaciones masivas

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. Puedes usar, modificar y distribuir este código libremente, incluso con fines comerciales. Solo se pide atribución. Para más detalles, consulta el archivo `LICENSE`.

## ✨ Autor

**Astharmin**

> "Automatizar no es eliminar el trabajo humano, es redirigirlo hacia donde más valor aporta."

---

⭐ **¿Te gusta automatizar tareas repetitivas? ¡Dale una estrella al repositorio para apoyar su desarrollo!** ⭐

*"Transformando horas de trabajo manual en segundos de procesamiento automático."*