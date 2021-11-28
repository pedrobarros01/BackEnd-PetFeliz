from flask_restful import Resource, reqparse

from models.adota import AdotaModel
import mysql.connector

class Adota(Resource):
    def post(self, cpf_cliente, cadastro_pet):
        adota = AdotaModel('SYSDATE()', 'NOW()', cadastro_pet, cpf_cliente)
        resultado_json = adota.realizar_adocao()
        return resultado_json


class PetsNaoAdotados(Resource):
    def get(self):
        connect = mysql.connector.connect(user='root', password='0',
                                      database='the_drungas')
        cursor = connect.cursor()
        consulta_pets_nao_adotados = "SELECT CADASTRO_PET, \
            NOME, DATA_NASCIMENTO, RACA, ESPECIE \
            FROM TB_PET WHERE EH_ADOTADO = TRUE"
        cursor.execute(consulta_pets_nao_adotados)
        resultado = cursor.fetchall()
        lista_nao_adotados= []
        if resultado:
            for linha in resultado:
                lista_nao_adotados.append(
                    {
                        'cadastro': linha[0],
                        'nome': linha[1],
                        'data_nascimento': str(linha[2]),
                        'raca': linha[3],
                        'especie': linha[4]
                    }
                )
        return {'messagem': lista_nao_adotados}, 200


