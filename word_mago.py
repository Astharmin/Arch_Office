import sys
import pandas as pd
from docxtpl import DocxTemplate

PLANTILLA_CURSOS_PATH = r'SRC/Plantilla_Final.docx'
PATH_OUTPUT = r'.\OUTPUT'

def main ():
    docs_tpl = DocxTemplate(PLANTILLA_CURSOS_PATH)
    context = {
        'curso' : '2021/2022',
        'nombre_alumno': 'Jose Torres',
        'clase': '4-C'
    }
    docs_tpl.render(context)
    docs_tpl.save(PATH_OUTPUT + r'\fichero_word.docx')

if __name__ == '__main__':
    main()