import pandas as pd
import os
import glob
# uma funcao de extract que le e consolida os json
from utils_log import log_decorator
from timer_decorator import time_measure_decorator
from tenacity_decorator import retry, stop_after_attempt, wait_fixed

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que transforma
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@time_measure_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)

@time_measure_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)

# uma funcao que da load em csv ou parquet
    
print(carregar_dados.__doc__)