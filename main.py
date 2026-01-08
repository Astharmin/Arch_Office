import pandas as pd


NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
# print(NOTAS_ALUMNOS)

def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS,
                             sheet_name='Notas')
    # print(excel_df)
    # for index, row in excel_df.iterrows():
    #     print(f'ID: {index} Nombre: {row['NOMBRE']}')

    asig_lista = list(excel_df['ASIGNATURA'].drop_duplicates())
    print(f'\nAsignaturas: {asig_lista}')

if __name__ == '__main__':
    main()