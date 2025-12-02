import pandas as pd


NOTAS_ALUMNOS = r'SRC/Notas_Alumnos.xlsx'
# print(NOTAS_ALUMNOS)

def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS,
                             sheet_name='Notas')
    # print(excel_df)
    for index, row in excel_df.iterrows():
        print(f'ID: {index} Nombre: {row['NOMBRE']}')

if __name__ == '__main__':
    main()