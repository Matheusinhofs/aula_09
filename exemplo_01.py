from loguru import logger
from sys import stderr
import os, pwd

username = pwd.getpwuid(os.getuid()).pw_name

# Configuração do logger para stderr
logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# Configuração do logger para arquivo de log
logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def soma(x,y):
    try:
        soma = x + y
        logger.info(f"Você obteve o total de {soma} com a função soma")
        return soma
    except:
        logger.critical("Você deve digitar valores corretos")
    

soma(2,3)
soma(2,6)
soma(2,"3")


logger.debug("Este é um aviso para o dev no debug")
logger.info("Traz alguma informação importante do processo")
logger.warning("Um aviso que algo vai deixar de funcionar no futuro")
logger.error("Ocorreu uma falha")
logger.critical("Aconteceu um erro que quebra a aplicação")

