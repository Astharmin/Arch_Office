import pandas as pd


NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
# print(NOTAS_ALUMNOS)

dict_asig = {
    'LENGUA CASTELLANA Y LITERATURA':   'Lengua Castellana y Literatura',
    'BIOLOGIA':                         'Biología',
    'GEOGRAFIA E HISTORIA':             'Geografía e Historia',
    'MATEMATICAS':                      'Matemáticas',
    'INGLES':                           'Inglés',
    'EDUCACION FISICA':                 'Educación Física',
    'ETICA':                            'Ética',
    'CULTURA CLASICA':                  'Cultura clásica',
    'MUSICA':                           'Música',
    'TECNOLOGIA':                       'Tecnología',
    'EDUCACION PLASTICA':               'Educación Plástica',
    'FRANCES':                          'Francés',
}

def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS,
                             sheet_name='Notas')
    # print(excel_df)
    # for index, row in excel_df.iterrows():
    #     print(f'ID: {index} Nombre: {row['NOMBRE']}')

    asig_lista = sorted(
        list(excel_df['ASIGNATURA'].drop_duplicates())
    )
    # print(f'\nAsignaturas: {asig_lista}')

    filtro = []
    for item in asig_lista:
        valorID = dict_asig[item]
        filtro.append(valorID)

    print(f'\nAsignaturas: {filtro}')

if __name__ == '__main__':
    main()