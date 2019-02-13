#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Este script tem como objetivo descriptografar os binários presentes no totem da Coca-Cola com o título de CR4CK TH3 COK3.
"""

# binário dos painéis
crack_the_code_01 = ['01001001', '01110011', '01110100', '01101111', '00100000', '01101110', '11100011', '01101111', '00100000', '11101001', '00100000', '01110101', '01101101', '01100001', '00100000', '01100100', '01101001', '01100011', '01100001', '00101100', '00100000', '01100110', '01101111', '01101001', '0100000', '01101101', '01100001', '01101100']
crack_the_code_02 = ['01000010', '01100001', '01101001', '01111000', '01100101', '00100000', '01101111', '00100000', '01100001', '01110000', '01110000', '00100000', '01100101', '01101101', '00100000', '01100011', '01110010', '01100001', '01100011', '01101011', '01110100', '01101000', '01100101', '01100011', '01101111', '01101011', '01100101', '00101110', '01100011', '01101111', '01101101', '00101110', '01100010', '01110010']
crack_the_code_03 = ['01010110', '01000001', '01001001', '00100000', '01001110', '01001111', '00100000', '01000111', '11000001', '01010011', '00100000', '01000011', '01000001', '01001101', '01010000', '01010101', '01010011', '00100000', '01010000', '01000001', '01010010', '01010100', '01011001']

# armazenando todos os paineis em uma lista
all_panels = [crack_the_code_01, crack_the_code_02, crack_the_code_03]


def binary_to_decimal(list_code):
    """
    Esta função tem como objetivo converter uma lista binária para uma lista em decimal.
    """

    # lista para retorno
    list_convert_decimal = []

    # para cada binário
    for binary in list_code:
        # converter para decimal
        list_convert_decimal.append(int(binary, 2))
        
    # retornadno a lista
    return list_convert_decimal


def decimal_to_char(list_code):
    """
    Esta função tem como objetivo converter uma lista de decimal para uma lista de caracteres.
    """
    
    # lista para retorno
    list_convert_char = []

    # para cada decimal
    for binary in list_code:
        # converter para caractere 
        list_convert_char.append(chr(binary))

    # retornando apenas uma string
    decrypt_char = ''.join(list_convert_char)

    return decrypt_char


def decrypt(list_codes):
    """
    Este programa tem como objetivo realizar a descriptografia para cada painel de código criptografado
    """

    # para cada painel em uma lista de paineis
    for index, panel in enumerate(all_panels):
        print('\n{}º painel: '.format(index+1))
        print(decimal_to_char(binary_to_decimal(panel)))


if __name__ == "__main__":
    """
    Programa main para centralizar todos o fluxo de código
    """

    # executando a descriptografia
    decrypt(all_panels)
