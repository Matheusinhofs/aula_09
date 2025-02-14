from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_argumento: str = 'dados'
formato_de_saida: list = ["csv","parquet"]

pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento, formato_de_saida)

