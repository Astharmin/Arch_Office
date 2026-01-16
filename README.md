# 📚 SchoolGuard: El Detective de Notas Escolares

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Validation-green.svg)
![Estado](https://img.shields.io/badge/Estado-En%20Producción-success.svg)
![Humor](https://img.shields.io/badge/Humor-Academicamente%20Gracioso-orange.svg)

## 🕵️‍♂️ ¿Qué es SchoolGuard?

**SchoolGuard** es tu detective personal de notas escolares. ¿Cansado de que Juan tenga 3 Matemáticas o de que María tenga notas de -5 a 15? ¡Este programa lo descubre todo! Es como un CSI pero para planillas de Excel académicas.

## 🎭 La Tragedia Cotidiana que Resolvemos

Imagina esto: Eres profesor/a y recibes un Excel con las notas. Pero...
- 📉 Pedro tiene 17 en Educación Física (¡quiere ir a las Olimpiadas!)
- 📚 Ana tiene 4 asignaturas de Inglés (¿bilingüe extremo?)
- ❌ A Carlos le "olvidaron" ponerle todas las asignaturas

**SchoolGuard** llega al rescate con su lupa digital para encontrar estos "errores creativos".

## ✨ Funcionalidades Detectivezcas

### 🔍 **Detección de Asignaturas Fantasmas**
```python
"⚠ Ana le faltan 3 asignaturas:"
"   • Matemáticas"
"   • Biología" 
"   • Ética"
```
*(Sospechoso... muy sospechoso)*

### 🔄 **Cazador de Duplicados**
```python
"⚠ Juan tiene asignaturas repetidas:"
"   • Educación Física: 3 veces"
```
*(¿Triple entrenamiento o error de copiar-pegar?)*

### 📊 **Policía de Notas**
```python
"⚠ Notas fuera de rango en NOTA T1:"
"   • Luis - Tecnología: 17.5"
```
*(¡Luis inventó una nueva escala de puntuación!)*

## 🏗️ Estructura del Proyecto

```
SchoolGuard/
├── 📁 SRC/
│   └── 📄 Notas_Alumnos.xlsx    # El archivo "sospechoso"
├── 🕵️‍♂️ detective_notas.py       # Nuestro detective principal
├── 📋 README.md                 # Esta documentación épica
└── ☕ requirements.txt          # Para el café... digo, dependencias
```

## 📋 Cómo Usar (Modo Detective)

```python
# Ejecuta y observa la magia:
python detective_notas.py

# Verás algo como:
============================================================
SISTEMA DE VALIDACIÓN DE NOTAS ACADÉMICAS
============================================================
📊 Datos cargados: 150 registros

============================================================
ASIGNATURAS ENCONTRADAS
============================================================
 1. Biología                    (25 alumnos)
 2. Cultura clásica             (22 alumnos)
 3. Educación Física            (25 alumnos)
 4. Educación Plástica          (24 alumnos)
... y así sucesivamente
```

## 🎯 ¿Qué Detecta Exactamente?

| Error | Ejemplo | Comentario del Detective |
|-------|---------|--------------------------|
| ⚠ **Notas imposibles** | Matemáticas: 17.5 | "¡Esta nota rompe las leyes de la física académica!" |
| ⚠ **Asignaturas fantasma** | Falta Inglés | "¿Vacaciones lingüísticas?" |
| ⚠ **Clones académicos** | 3x Educación Física | "¿Entrenamiento para trilogía deportiva?" |

## 🎨 Características Especiales

### 📚 **Traductor de Asignaturas**
```python
dict_asig = {
    'MATEMATICAS': 'Matemáticas',  # Sin acento → Con acento
    'INGLES': 'Inglés',            # Porque la ortografía importa
    'ETICA': 'Ética',              # Incluso en mayúsculas
}
```
*(Porque escribir bien es de gente educada)*

### 📊 **Estadísticas en Tiempo Real**
```
Total de alumnos: 25
Total de asignaturas: 12
Total registros válidos: 300
```
*(¡Matemáticas que sí tienen sentido!)*

## 🚨 Casos de Uso Realistas

### **Caso 1: El Alumno Invisible**
```python
"⚠ Pedro le faltan 5 asignaturas"
# Diagnóstico: ¿Se escapó a mitad de año?
```

### **Caso 2: El Sobresaliente Exagerado**
```python
"⚠ Notas fuera de rango: Tecnología: 25"
# Diagnóstico: ¡Inventó una máquina del tiempo!
```

### **Caso 3: El Amante de las Asignaturas**
```python
"⚠ María tiene asignaturas repetidas: Música: 4 veces"
# Diagnóstico: ¿Cuarteto musical o error de Excel?
```

## 🔧 Para Desarrolladores (Modo Serio)

### **Estructura del Código**
```python
def validar_estructura(df):
    """Valida la estructura completa del DataFrame"""
    # 1. Verifica asignaturas por alumno
    # 2. Busca duplicados
    # 3. Valida rangos de notas
    # 4. Reporta como un detective educado
```

### **Extender el Detective**
```python
# ¿Quieres agregar más validaciones?
def validar_promedios(df):
    """Detecta promedios sospechosamente perfectos"""
    pass

def validar_evolucion(df):
    """Analiza si las notas mejoran/deterioran sospechosamente"""
    pass
```

## 📈 Próximas Actualizaciones

- [ ] 🎯 **Modo Paranoico**: Detectar si alguien tiene todas las notas iguales
- [ ] 📱 **Interfaz Web**: Para que los directores lo usen sin saber programar
- [ ] 🤖 **IA Predictiva**: "Este alumno tiene un 87% de probabilidad de copiar"
- [ ] 🎮 **Modo Juego**: "Encuentra los 10 errores en esta planilla"

## 🤝 ¿Quieres Contribuir?

¡Claro que sí! Puedes:
1. 🐛 Reportar un "crimen académico" no detectado (bug)
2. 💡 Sugerir nuevas validaciones detectivezcas
3. 📝 Mejorar la documentación (más chistes, por favor)
4. 🔧 Añadir funcionalidades (¿validación de asistencia?)

## 📜 Licencia

Licencia MIT - Básicamente: "Úsalo, mejóralo, compártelo, pero no culpes al detective si alguien reprueba".

## ✨ Autor

**Astharmin** - El detective que prefirió Python sobre una lupa real.

> "En un mundo lleno de datos desordenados, alguien tiene que poner orden... y un poco de humor."

---

⭐ **¿Te gustó este detective académico? ¡Dale una estrella al repositorio!** ⭐

*"Validando notas desde 2023, porque 2+2 nunca fue 5... a menos que sea en Excel"*
