import pandas as pd

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


def detec(df):
    #<--- Detectar asignaturas faltantes o repetidas --->
    alum_list = sorted(list(df['NOMBRE'].drop_duplicates()))
    asig_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))

    #<--- Detectar notas vacias o repetidas --->
    for al in alum_list:
        for asig in asig_list:
            filtro_all = df[(df['NOMBRE'] == al) & (df['ASIGNATURA'] == asig)]

            if len(filtro_all) == 0:
                print(f'Error: {al} no tiene asignatura: {asig}')
            elif len(filtro_all) > 1:
                print(f'Error: {al} asignatura repetida: {asig, len(filtro_all)}')

    #<--- Detectar notas fuera de rango --->
    for index, row in df.iterrows():
        alumno = row['NOMBRE']
        asignatura = row['ASIGNATURA']
        trimestre_list = ['NOTA T1', 'NOTA T2', 'NOTA T3']

        for trim in trimestre_list:
            nota = row[trim]
            if not (0.0 <= nota <= 10.0):
                print(f'Error: {alumno} tiene nota {trim}, '
                      f'asignatura: {asignatura} fuera de rango: {nota}')


def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS, sheet_name='Notas')

    asig_lista = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))

    filtro = []
    for item in asig_lista:
        valorID = dict_asig[item]
        filtro.append(valorID)

    print(f'\nAsignaturas: {filtro}\n')

    detec(excel_df)


if __name__ == '__main__':
    main()