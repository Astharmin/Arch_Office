import pandas as pd
import shutil, os
from docxtpl import DocxTemplate

NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
PLANTILLA_CURSOS_PATH = r'SRC/Plantilla_Final.docx'
PATH_OUTPUT = r'.\OUTPUT'

curso = '2021/2025'
df = pd.read_excel(NOTAS_ALUMNOS, sheet_name='Datos_Alumnos')
nom_alum_list = sorted(df['NOMBRE'].dropna().unique())
# nom_alumnos = nom_alum_list[0]

def elminar_tildes(texto):
    tildes_dic = {
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
    }
    texto_lim = texto

    for key in tildes_dic:
        texto_lim = texto_lim.replace(key, tildes_dic[key])

    return texto_lim

def control_arch(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)

def main ():
    control_arch(PATH_OUTPUT)

    for nom_alumnos in nom_alum_list:
        filt_datos_alum = df[(df['NOMBRE'] == nom_alumnos)]
        clase = filt_datos_alum.iloc[0]['CLASE']

        docs_tpl = DocxTemplate(PLANTILLA_CURSOS_PATH)
        context = {
            'curso' : curso,
            'nombre_alumno': nom_alumnos,
            'clase': clase
        }
        docs_tpl.render(context)

        titulo = 'NOTAS_'+nom_alumnos.replace(' ', '_').upper()
        titulo = elminar_tildes(titulo)
        titulo += '.docx'

        docs_tpl.save(PATH_OUTPUT + '\\' + titulo)

if __name__ == '__main__':
    main()