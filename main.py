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

def detec(df):

    alum_list = sorted(list(
        df['NOMBRE'].drop_duplicates()
    ))
    asig_list = sorted(list(
        df['ASIGNATURA'].drop_duplicates()
    ))

    for al in alum_list:
        for asig in asig_list:
            filtro_all = df[(df['NOMBRE'] == al) & (df['ASIGNATURA'] == asig)]
            # print(f'Nombre y Asignatura: {filtro_all}')

            if len(filtro_all) == 0:
                print(f'Error: {al} no tiene asignatura: {asig}')
            elif len(filtro_all) > 1:
                print(f'Error: {al} asignatura repetida: {asig, len(filtro_all)}')

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

    detec(excel_df)

if __name__ == '__main__':
    main()