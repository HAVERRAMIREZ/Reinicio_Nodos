import os
import pandas as pd
import datetime
import easygui  # Importa el módulo easygui para usar una interfaz gráfica

def obtener_archivo_mas_reciente(ruta_carpeta, nombre_base):
    archivos = [archivo for archivo in os.listdir(ruta_carpeta) if nombre_base in archivo]
    if archivos:
        archivo_mas_reciente = max(archivos, key=lambda x: os.path.getctime(os.path.join(ruta_carpeta, x)))
        return os.path.join(ruta_carpeta, archivo_mas_reciente)
    return None

def ejecutar_todo(ruta_descargas, nombre_base):
    # Ruta de la carpeta donde se guardarán los archivos CSV
    carpeta_destino = r"C:\reinicios"

    # Verifica si la carpeta destino existe, si no, créala
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    df1 = pd.read_excel(r"C:\Users\hramb\Downloads\data (6).xlsx")
    df2 = pd.read_excel(r"C:\Users\hramb\Downloads\data (7).xlsx")

    # Filtra las filas según la prioridad (P1 o P2) y selecciona la columna "DN"
    df1_prioridad_1 = df1[df1["Prioridades"] == "P1"]["DN"].unique()
    df1_prioridad_2 = df1[df1["Prioridades"] == "P2"]["DN"].unique()
    df2_prioridad_1 = df2[df2["Prioridades"] == "P1"]["DN"].unique()
    df2_prioridad_2 = df2[df2["Prioridades"] == "P2"]["DN"].unique()

    # Concatena los DataFrames filtrados
    df_combined = pd.concat([
        pd.DataFrame({"Prioridades": "P1", "DN": df1_prioridad_1}),
        pd.DataFrame({"Prioridades": "P2", "DN": df1_prioridad_2}),
        pd.DataFrame({"Prioridades": "P1", "DN": df2_prioridad_1}),
        pd.DataFrame({"Prioridades": "P2", "DN": df2_prioridad_2})
    ])

    # Elimina valores nulos en la columna "DN"
    df_combined = df_combined.dropna(subset=["DN"])

    # Elimina duplicados en la columna "DN"
    df_combined = df_combined.drop_duplicates("DN")

    # Agrega una columna llamada "8" y llena todas sus celdas con el valor 8
    df_combined["8"] = 8

    # Reordena las columnas para que "8" esté al inicio
    df_combined = df_combined[["8", "DN"]]

    # Obtener la ruta del archivo a comparar
    archivo_comparar = obtener_archivo_mas_reciente(ruta_descargas, nombre_base)

    if archivo_comparar:
        print(f"Se encontró el archivo más reciente: {archivo_comparar}")
    else:
        print("No se encontró ningún archivo con el nombre base especificado.")
        return

    # Realiza la última comparación con el archivo más reciente
    df_comparar = pd.read_excel(archivo_comparar)
    df_combined = comparar_dn(df_combined, df_comparar)

    # Divide el DataFrame en grupos de 90 registros
    grupos = [df_combined[i:i+90] for i in range(0, len(df_combined), 90)]

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Construir el nombre del archivo con el formato deseado
    nombre_archivo = os.path.join(carpeta_destino, f"Reinicios_{fecha_actual}.csv")

    # Guarda cada grupo como un archivo CSV en la carpeta destino
    for i, grupo in enumerate(grupos):
        grupo.to_csv(nombre_archivo, index=False)
        print(f"Se ha generado el archivo {nombre_archivo} en la carpeta destino con éxito.")

    # Imprime un mensaje de confirmación
    print("Se han generado todos los archivos en la carpeta destino con éxito.")

def comparar_dn(df_combined, df_comparar):
    # Realiza la comparación de los DN y elimina las coincidencias
    coincidencias = set(df_combined["DN"]).intersection(df_comparar["DN"])
    df_combined = df_combined[~df_combined["DN"].isin(coincidencias)]
    return df_combined

# Solicitar al usuario la ruta de la carpeta de descargas
ruta_descargas = easygui.diropenbox("Selecciona la carpeta de descargas:")

# Nombre base que se utilizará en el código
nombre_base = "Export-Maximo_FlujosNOW"

# Llamar a la función para ejecutar todo el proceso con los valores ingresados por el usuario
ejecutar_todo(ruta_descargas, nombre_base)
