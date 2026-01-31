import pandas as pd
import shutil
import os
from docxtpl import DocxTemplate
from pathlib import Path

# Constantes de configuración
NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
PLANTILLA_CURSOS_PATH = r'SRC/Plantilla_Final.docx'
PATH_OUTPUT = r'.\OUTPUT'
CURSO = '2021/2025'


def eliminar_tildes(texto: str) -> str:
    tildes_dic = {
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Ñ': 'N', 'ñ': 'n'
    }

    texto_limpio = texto
    for tilde, sin_tilde in tildes_dic.items():
        texto_limpio = texto_limpio.replace(tilde, sin_tilde)

    return texto_limpio


def preparar_directorio_salida(ruta_salida: str) -> None:
    ruta = Path(ruta_salida)

    if ruta.exists():
        print(f"Limpiando directorio existente: {ruta_salida}")
        shutil.rmtree(ruta)

    ruta.mkdir(parents=True, exist_ok=True)
    print(f"Directorio listo: {ruta_salida}")


def cargar_y_combinar_datos_excel(ruta_excel: str) -> pd.DataFrame:
    try:
        # Cargar datos de notas (hoja 'Notas')
        df_notas = pd.read_excel(ruta_excel, sheet_name='Notas')
        print(f"Datos de notas cargados: {len(df_notas)} registros")

        # Cargar datos de alumnos (hoja 'Datos_Alumnos')
        df_alumnos = pd.read_excel(ruta_excel, sheet_name='Datos_Alumnos')
        print(f"Datos de alumnos cargados: {len(df_alumnos)} registros")

        # Combinar los DataFrames por el nombre del alumno
        df_combinado = pd.merge(df_notas, df_alumnos, on='NOMBRE', how='left')
        print(f"Datos combinados: {len(df_combinado)} registros")

        # Verificar que todos los alumnos tengan clase asignada
        sin_clase = df_combinado['CLASE'].isna().sum()
        if sin_clase > 0:
            print(f"ADVERTENCIA: {sin_clase} registros sin clase asignada")

        return df_combinado

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo {ruta_excel}")
        raise
    except Exception as e:
        print(f"ERROR al cargar datos: {e}")
        raise


def obtener_lista_alumnos(df: pd.DataFrame) -> list:
    nombres = df['NOMBRE'].dropna().unique()
    return sorted(nombres)


def filtrar_datos_alumno(df: pd.DataFrame, nombre_alumno: str) -> tuple:
    datos_alumno = df[df['NOMBRE'] == nombre_alumno]

    if datos_alumno.empty:
        raise ValueError(f"No se encontraron datos para: {nombre_alumno}")

    clase = datos_alumno.iloc[0]['CLASE']
    return datos_alumno, clase


def generar_nombre_archivo(nombre_alumno: str) -> str:
    nombre_sin_tildes = eliminar_tildes(nombre_alumno)
    nombre_archivo = f"NOTAS_{nombre_sin_tildes.replace(' ', '_').upper()}.docx"
    return nombre_archivo


def extraer_asignaturas_notas(df_alumno: pd.DataFrame) -> list:
    asig_list = []

    # Obtener asignaturas únicas del alumno
    asignaturas = df_alumno['ASIGNATURA'].dropna().unique()

    for asig in sorted(asignaturas):
        # Filtrar datos para esta asignatura
        datos_asig = df_alumno[df_alumno['ASIGNATURA'] == asig]

        if not datos_asig.empty:
            fila = datos_asig.iloc[0]

            # Extraer notas de cada trimestre
            nota_t1 = fila.get('NOTA T1', '')
            nota_t2 = fila.get('NOTA T2', '')
            nota_t3 = fila.get('NOTA T3', '')

            # Calcular promedio solo si hay notas numéricas
            notas_numericas = []
            for nota in [nota_t1, nota_t2, nota_t3]:
                if isinstance(nota, (int, float)) and pd.notna(nota):
                    notas_numericas.append(float(nota))

            nota_final = round(sum(notas_numericas) / len(notas_numericas), 2) if notas_numericas else 0.0

            item = {
                'nombre_asignatura': asig,
                'asignombre_asignatura': asig,
                't1': nota_t1 if pd.notna(nota_t1) else '',
                't2': nota_t2 if pd.notna(nota_t2) else '',
                't3': nota_t3 if pd.notna(nota_t3) else '',
                'nota_final': nota_final,
                'calificaciones': ''
            }

            asig_list.append(item)

    return asig_list


def crear_contexto_documento(nombre_alumno: str, clase: str, asignaturas: list) -> dict:
    return {
        'curso': CURSO,
        'nombre_alumno': nombre_alumno,
        'clase': clase,
        'asignatura': asignaturas
    }


def generar_documento_individual(
        plantilla_path: str,
        contexto: dict,
        ruta_salida: str,
        nombre_archivo: str
) -> str:
    try:
        # Cargar plantilla
        documento = DocxTemplate(plantilla_path)

        # Verificar si hay etiquetas problemáticas en la plantilla
        with open(plantilla_path, 'rb') as f:
            content = f.read()
            if b'{{%' in content or b'%}}' in content:
                print(f"ADVERTENCIA: La plantilla contiene sintaxis Jinja2 incorrecta")

        documento.render(contexto)

        # Guardar documento
        ruta_completa = Path(ruta_salida) / nombre_archivo
        documento.save(str(ruta_completa))

        return str(ruta_completa)

    except Exception as e:
        raise Exception(f"Error al generar documento: {e}")


def procesar_alumno(
        df: pd.DataFrame,
        nombre_alumno: str,
        plantilla_path: str,
        ruta_salida: str
) -> tuple:
    try:
        # Obtener datos del alumno
        datos_alumno, clase = filtrar_datos_alumno(df, nombre_alumno)

        # Extraer asignaturas y notas
        asignaturas = extraer_asignaturas_notas(datos_alumno)

        # Crear contexto con las asignaturas
        contexto = crear_contexto_documento(nombre_alumno, clase, asignaturas)

        # Generar nombre de archivo
        nombre_archivo = generar_nombre_archivo(nombre_alumno)

        # Crear documento
        ruta_documento = generar_documento_individual(
            plantilla_path, contexto, ruta_salida, nombre_archivo
        )

        return nombre_alumno, ruta_documento, None

    except Exception as e:
        return nombre_alumno, None, str(e)


def mostrar_progreso(indice: int,
                     total: int,
                     nombre_alumno: str,
                     exito: bool, error: str = None):
    if exito:
        print(f"[{indice:3d}/{total}] ✅ {nombre_alumno}")
    else:
        print(f"[{indice:3d}/{total}] ❌ {nombre_alumno} - Error: {error}")


def generar_resumen_proceso(resultados: list, ruta_salida: str):
    exitosos = sum(1 for r in resultados if r[1] is not None)
    fallidos = len(resultados) - exitosos

    print("\n" + "=" * 60)
    print("RESUMEN DEL PROCESO")
    print("=" * 60)
    print(f"Total alumnos procesados: {len(resultados)}")
    print(f"Documentos generados: {exitosos}")
    print(f"Errores: {fallidos}")

    # Guardar resumen en archivo
    ruta_resumen = Path(ruta_salida) / "resumen_proceso.txt"
    with open(ruta_resumen, 'w', encoding='utf-8') as f:
        f.write("Resumen de generación de documentos\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Fecha: {pd.Timestamp.now()}\n")
        f.write(f"Total alumnos: {len(resultados)}\n")
        f.write(f"Exitosos: {exitosos}\n")
        f.write(f"Fallidos: {fallidos}\n\n")

        if fallidos > 0:
            f.write("Errores encontrados:\n")
            for nombre, _, error in resultados:
                if error:
                    f.write(f"- {nombre}: {error}\n")

    print(f"\nResumen guardado en: {ruta_resumen}")


def main():
    print("=" * 60)
    print("GENERADOR DE DOCUMENTOS DE NOTAS")
    print("=" * 60)

    try:
        # 1. Preparar directorio de salida
        preparar_directorio_salida(PATH_OUTPUT)

        # 2. Cargar y combinar datos del Excel
        df = cargar_y_combinar_datos_excel(NOTAS_ALUMNOS)

        # 3. Obtener lista de alumnos
        nombres_alumnos = obtener_lista_alumnos(df)
        total_alumnos = len(nombres_alumnos)

        print(f"\nProcesando {total_alumnos} alumnos...")
        print("-" * 50)

        # 4. Procesar cada alumno
        resultados = []

        for i, nombre_alumno in enumerate(nombres_alumnos, 1):
            # Procesar alumno
            nombre, ruta_doc, error = procesar_alumno(
                df, nombre_alumno, PLANTILLA_CURSOS_PATH, PATH_OUTPUT
            )

            # Mostrar progreso
            mostrar_progreso(i, total_alumnos, nombre, error is None, error)

            # Guardar resultado
            resultados.append((nombre, ruta_doc, error))

        # 5. Generar resumen
        generar_resumen_proceso(resultados, PATH_OUTPUT)

        print("\n✅ Proceso completado!")

    except Exception as e:
        print(f"\n❌ Error en el proceso principal: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())