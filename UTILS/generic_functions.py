"""

    FUNÇÕES GENÉRICAS UTILIZANDO PYTHON.

    # Arguments

    # Returns


"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "04/07/2021"


import datetime
from inspect import stack
from os import path, makedirs, walk, getcwd
import time
from unidecode import unidecode

import pandas as pd


def verify_exists(dir):

    """

        FUNÇÃO PARA VERIFICAR SE UM DIRETÓRIO (PATH) EXISTE.

        # Arguments
            dir                  - Required : Diretório a ser verificado (String)

        # Returns
            validador            - Required : Validador da função (Boolean)

    """

    # INICIANDO O VALIDADOR DA FUNÇÃO
    validador = False

    try:
        validador = path.exists(dir)
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return validador


def get_files_directory(path_dir, specific_type=None):

    """

        FUNÇÃO PARA OBTER ARQUIVOS DE UM DIRETÓRIO.

        É POSSÍVEL ENVIAR UM FORMATO ESPECÍFICO PARA
        FILTRO DO FORMATO DE ARQUIVO DESEJADO.
        EX: OBTER APENAS JPGS

        # Arguments
            path_dir                   - Required : Diretório analisado (String)
            specific_type              - Optional : Lista com os formatos desejados (List)

        # Returns
            list_files                 - Required : Arquivos do diretório (List)

    """

    # INICIANDO A VARIÁVEL QUE ARMAZENARÁ TODOS OS ARQUIVOS DO DIRETÓRIO
    list_files = []

    # OBTENDO TODOS OS ARQUIVOS
    try:

        # VERIFICANDO SE É DIRETÓRIO
        if path.isdir(path_dir):

            list_files = [path.join(path_dir, name) for name in listdir(path_dir)]

            if specific_type:

                if not isinstance(specific_type, tuple):
                    specific_type = tuple(specific_type)

                list_files = [arq for arq in list_files if arq.lower().endswith((specific_type))]

        else:
            list_files = [path_dir]

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return list_files


def create_path(dir):

    """

        FUNÇÃO PARA CRIAR UM DIRETÓRIO (PATH).

        # Arguments
            dir                  - Required : Diretório a ser criado (String)

        # Returns
            validador            - Required : Validador da função (Boolean)

    """

    # INICIANDO O VALIDADOR DA FUNÇÃO
    validador = False

    try:
       # REALIZANDO A CRIAÇÃO DO DIRETÓRIO
       makedirs(dir)

       validador = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return validador


def converte_int(valor_para_converter):

    """

        FUNÇÃO GENÉRICA PARA CONVERTER UM VALOR PARA FORMATO INTEIRO.


        # Arguments
            valor_para_converter              - Required : Valor para converter (Object)

        # Returns
            valor_para_converter              - Required : Valor após conversão (Integer)

    """

    try:
        if isinstance(valor_para_converter, int):
            return valor_para_converter
        else:
            return int(valor_para_converter)
    except Exception as ex:
        print(ex)
        return None


def get_split_dir(dir):

    """

        USADO PARA DIVIDIR O NOME DO CAMINHO EM UM PAR DE CABEÇA E CAUDA.
        AQUI, CAUDA É O ÚLTIMO COMPONENTE DO NOME DO CAMINHO E CABEÇA É TUDO QUE LEVA A ISSO.

        EX: nome do caminho = '/home/User/Desktop/file.txt'
        CABEÇA: '/home/User/Desktop'
        CAUDA: 'file.txt'

        * O DIR PODE SER UMA BASE64

        # Arguments
            dir                 - Required : Caminho a ser splitado (String)

        # Returns
            directory           - Required : Cabeça do diretório (String)
            filename            - Required : Cauda do diretório (String)

    """

    # INICIANDO AS VARIÁVEIS A SEREM OBTIDAS
    directory = filename = None

    try:
        directory, filename = path.split(dir)
    except Exception as ex:
        print(ex)

    return directory, filename


def read_csv(data_dir):

    """

        REALIZA LEITURA DA BASE (CSV)

        # Arguments
            data_dir                      - Required : Diretório da base a ser lida (String)

        # Returns
            validador                     - Required : Validação da função (Boolean)
            dataframe                     - Required : Base lida (DataFrame)

    """

    # INICIANDO O VALIDADOR
    validador = False

    # INICIANDO O DATAFRAME DE RESULTADO DA LEITURA
    dataframe = pd.DataFrame()

    try:
        dataframe = pd.read_csv(data_dir, encoding='utf-8')

        validador = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validador, dataframe


def save_excel(dataframe_to_save, data_dir):

    """

        REALIZA SAVE DA BASE (CSV)

        # Arguments
            dataframe_to_save             - Required : Base a ser salva (DataFrame)
            data_dir                      - Required : Diretório da base a ser salva (String)

        # Returns
            validador                     - Required : Validação da função (Boolean)

    """

    # INICIANDO O VALIDADOR
    validador = False

    try:
        dataframe_to_save.to_excel(data_dir, index=None)

        validador = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validador


def get_date_time_now(return_type):

    """

        OBTÉM TODOS OS POSSÍVEIS RETORNOS DE DATA E TEMPO.

        # Arguments
            return_type                    - Required : Formato de retorno. (String)

        # Returns

    """

    """%d/%m/%Y %H:%M:%S | %Y-%m-%d %H:%M:%S
    Dia: %d
    Mês: %
    Ano: %Y
    Data: %Y/%m/%d

    Hora: %H
    Minuto: %M
    Segundo: %S"""

    try:
        ts = time.time()
        stfim = datetime.datetime.fromtimestamp(ts).strftime(return_type)

        return stfim
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))
        return datetime.datetime.now()


def verify_find_intersection(data_verified, data_lists):

    """

        FUNÇÃO PARA VERIFICAR SE UM DADO (DATA_VERIFIED) ESTÁ CONTIDO
        EM QUALQUER ELEMENTO DE UMA LISTA DE DADOS.

        ESSA VERIFICAÇÃO É REALIZADA UTILIZANDO PARTE DA STRING,
        NESSE CASO, UTILIZA-SE O MÉTODO 'FIND'.

        # Arguments
            data_verified               - Required : Dado a ser verificado (String)
            data_lists                  - Required : Lista de dados (List)

        # Returns
            validador                   - Required : Validador da função (String)

    """

    # INICIANDO O VALIDADOR DA FUNÇÃO
    validador = False

    try:
        # PERCORRENDO TODOS OS DADOS DA LISTA DE DADOS
        for value in data_lists:

            # VERIFICANDO SE O VALOR A SER VERIFICADO ESTÁ CONTIDO NA LISTA DE DADOS
            # ESSA VERIFICAÇÃO É REALIZADA UTILIZANDO PARTE DA STRING
            # NESSE CASO, UTILIZA-SE O MÉTODO 'FIND'
            if data_verified.find(value) != -1 and data_verified != "":
                validador = True
                break

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validador


def convert_text_unidecode(text):

    """

        TRANSFORMA O TEXTO PURO EM FORMATO UNIDECODE (SEM ACENTOS).

        # Arguments
            text                    - Required : Texto a ser convertido. (String)

        # Returns
            text_unidecode          - Required : Texto após conversão. (String)

    """

    try:
        return unidecode(text)
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))
        return text