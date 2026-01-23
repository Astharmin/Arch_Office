import sys
import pandas as pd
from docxtpl import DocxTemplate

NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
PLANTILLA_CURSOS_PATH = r'SRC/Plantilla_Final.docx'
PATH_OUTPUT = r'.\OUTPUT'

curso = '2021/2022'
df = pd.read_excel(NOTAS_ALUMNOS, sheet_name='Datos_Alumnos')
nom_alum_list = sorted(df['NOMBRE'].dropna().unique())
nom_alumnos = nom_alum_list[0]

def main ():
    docs_tpl = DocxTemplate(PLANTILLA_CURSOS_PATH)
    context = {
        'curso' : curso,
        'nombre_alumno': nom_alumnos,
        'clase': '4-C'
    }
    docs_tpl.render(context)
    docs_tpl.save(PATH_OUTPUT + r'\fichero_word.docx')

if __name__ == '__main__':
    main()