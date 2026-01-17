import pandas as pd
import sys
from typing import Dict, List, Tuple

NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'

dict_asig = {
    'LENGUA CASTELLANA Y LITERATURA': 'Lengua Castellana y Literatura',
    'BIOLOGIA': 'Biología',
    'GEOGRAFIA E HISTORIA': 'Geografía e Historia',
    'MATEMATICAS': 'Matemáticas',
    'INGLES': 'Inglés',
    'EDUCACION FISICA': 'Educación Física',
    'ETICA': 'Ética',
    'CULTURA CLASICA': 'Cultura clásica',
    'MUSICA': 'Música',
    'TECNOLOGIA': 'Tecnología',
    'EDUCACION PLASTICA': 'Educación Plástica',
    'FRANCES': 'Francés',
}


def validar_estructura(df: pd.DataFrame) -> Tuple[bool, bool, bool]:
    """
    Valida la estructura completa del DataFrame de notas.

    Returns:
        Tuple[bool, bool, bool]:
            - err_faltantes: True si hay asignaturas faltantes
            - err_repetidas: True si hay asignaturas repetidas
            - err_rango: True si hay notas fuera de rango
    """
    err_faltantes, err_repetidas, err_rango = False, False, False

    # Obtener listas únicas
    alumnos = df['NOMBRE'].dropna().unique()
    asignaturas = df['ASIGNATURA'].dropna().unique()

    print("=" * 60)
    print("VALIDACIÓN DE ESTRUCTURA DE DATOS")
    print("=" * 60)
    print(f"Total de alumnos: {len(alumnos)}")
    print(f"Total de asignaturas: {len(asignaturas)}")
    print("-" * 60)

    # Validar asignaturas por alumno
    for alumno in alumnos:
        asig_alumno = df[df['NOMBRE'] == alumno]['ASIGNATURA'].unique()

        # Verificar asignaturas faltantes
        faltantes = set(asignaturas) - set(asig_alumno)
        if faltantes:
            print(f"⚠ {alumno} le faltan {len(faltantes)} asignaturas:")
            for asig in sorted(faltantes):
                print(f"   • {dict_asig.get(asig, asig)}")
            err_faltantes = True

        # Verificar asignaturas repetidas
        conteo_asig = df[df['NOMBRE'] == alumno]['ASIGNATURA'].value_counts()
        repetidas = conteo_asig[conteo_asig > 1]
        if not repetidas.empty:
            print(f"⚠ {alumno} tiene asignaturas repetidas:")
            for asig, cantidad in repetidas.items():
                print(f"   • {dict_asig.get(asig, asig)}: {cantidad} veces")
            err_repetidas = True

    # Validar rango de notas
    print("-" * 60)
    print("VALIDACIÓN DE RANGO DE NOTAS")
    print("-" * 60)

    for trimestre in ['NOTA T1', 'NOTA T2', 'NOTA T3']:
        notas_fuera_rango = df[~df[trimestre].between(0, 10, inclusive='both')]

        if not notas_fuera_rango.empty:
            print(f"⚠ Notas fuera de rango en {trimestre}: {len(notas_fuera_rango)}")
            for _, row in notas_fuera_rango.iterrows():
                print(f"   • {row['NOMBRE']} - {dict_asig.get(row['ASIGNATURA'], row['ASIGNATURA'])}: {row[trimestre]}")
            err_rango = True

    return err_faltantes, err_repetidas, err_rango


def validar_datos(df: pd.DataFrame) -> bool:
    errores = validar_estructura(df)

    # Resumen de validación
    print("\n" + "=" * 60)
    print("RESUMEN DE VALIDACIÓN")
    print("=" * 60)

    total_errores = sum(errores)

    if total_errores == 0:
        print("✅ TODAS LAS VALIDACIONES PASARON CORRECTAMENTE")
        print(f"✓ Estructura de datos: OK")
        print(f"✓ Rango de notas: OK")
        print(f"✓ Total registros válidos: {len(df)}")
        return True
    else:
        print(f"❌ SE ENCONTRARON {total_errores} TIPO(S) DE ERRORES:")
        if errores[0]:
            print("   • Asignaturas faltantes por alumno")
        if errores[1]:
            print("   • Asignaturas duplicadas por alumno")
        if errores[2]:
            print("   • Notas fuera del rango permitido (0-10)")

        print("\n🔧 CORRECCIÓN NECESARIA:")
        print("  1. Revise el archivo Excel original")
        print("  2. Corrija los errores listados arriba")
        print("  3. Ejecute nuevamente la validación")

        return False


def cargar_datos() -> pd.DataFrame:
    """Carga y prepara los datos del archivo Excel."""
    try:
        df = pd.read_excel(NOTAS_ALUMNOS, sheet_name='Notas')

        # Limpieza básica
        df = df.dropna(subset=['NOMBRE', 'ASIGNATURA'])
        df['NOMBRE'] = df['NOMBRE'].str.strip()
        df['ASIGNATURA'] = df['ASIGNATURA'].str.strip()

        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{NOTAS_ALUMNOS}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        sys.exit(1)


def mostrar_asignaturas(df: pd.DataFrame):
    """Muestra las asignaturas encontradas en formato legible."""
    asignaturas = sorted(df['ASIGNATURA'].dropna().unique())

    print("\n" + "=" * 60)
    print("ASIGNATURAS ENCONTRADAS")
    print("=" * 60)

    for i, asig in enumerate(asignaturas, 1):
        nombre_legible = dict_asig.get(asig, asig)
        # Contar alumnos por asignatura
        total_alumnos = df[df['ASIGNATURA'] == asig]['NOMBRE'].nunique()
        print(f"{i:2d}. {nombre_legible:<30} ({total_alumnos} alumnos)")

    print("-" * 60)
    print(f"Total: {len(asignaturas)} asignaturas diferentes")


def main():
    """Función principal del programa."""
    print("=" * 60)
    print("SISTEMA DE VALIDACIÓN DE NOTAS ACADÉMICAS")
    print("=" * 60)

    # Cargar datos
    df = cargar_datos()
    print(f"📊 Datos cargados: {len(df)} registros")

    # Mostrar asignaturas
    mostrar_asignaturas(df)

    # Validar datos
    print("\n" + "=" * 60)
    print("INICIANDO VALIDACIÓN...")
    print("=" * 60)

    if not validar_datos(df):
        print("\n" + "=" * 60)
        print("VALIDACIÓN FALLIDA - CORRIJA LOS ERRORES")
        print("=" * 60)
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ VALIDACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 60)
    print("\nPuede proceder con el análisis de datos.")


if __name__ == '__main__':
    main()