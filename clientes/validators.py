# Validações para os campos do serializers
# Tambem podemos passar as validações direto no serializer.py
# Porem resolvemos deixar os arquivos o mais limpo possível

# def validate_cpf(self, cpf):
#     if len(cpf) != 11:
#         raise serializers.ValidationError("O cpf deve ter 11 digitos")
#     return cpf

# def validate_nome(self, nome):
#     if not nome.isalpha():
#         raise serializer.ValidationError("Deve apenas ter letras")
#     return nome



import re 
from validate_docbr import CPF

# Validações isoladas

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)   

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
        return len(rg) != 9
         
def celular_valido(celular):
    """Verifica se o celular é válido (19 99878-8547)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta        