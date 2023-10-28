from pycpfcnpj import cpfcnpj
from pycep import PyCep
import re

class Validate:
    def __init__(self):
        pass

    def validate_cpfcnpj(self, documento):
        if len(documento) == 14: # 14 to CPF
            return cpfcnpj.validate(documento)
        elif len(documento) == 18: # 18 to CNPJ
            return cpfcnpj.validate(documento)
        else:
            return False

    def validate_cep(self, cep):
        logradouro = 0
        cidade = 0
        bairro = 0
        list = ['logradouro', 'bairro', 'localidade']
        x = 0

        if len(cep) == 9:
            cep1 = PyCep(cep)

            keys = cep1.dadosCep.keys()
            if 'logradouro' in keys:
                for i in list:
                    get_value = cep1.dadosCep.get(i)
                    match x:
                        case 0:
                            logradouro = get_value
                        case 1:
                            bairro = get_value
                        case 2:
                            cidade = get_value
                    x += 1
                return cep1, logradouro, bairro, cidade
            else:
                return False
        else:
            return False

class StrManipulate:
    def __init__(self):
        pass

    @staticmethod
    def split_url_in_string(string):
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\,]|)+')
        url = re.findall(url_pattern, string)
        return str(url)

    @staticmethod
    def split_wpp_url_in_string(string):
        print(string)
        url_pattern = re.compile(r'https://wa\.me/\d+')
        urls = re.findall(url_pattern, string)
        print(urls)
        return str(urls)