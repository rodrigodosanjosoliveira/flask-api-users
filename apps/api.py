# -*- coding: utf-8 -*-

# Third
# Importamos as classes API e Resource
from flask_restful import Api, Resource


# Criamos uma classe que extende de Resource
class Index(Resource):

    # Definimos a operação get do protocolo http
    def get(self):

        # retornamos um simples dicionário que será automaticamente
        # retornado em json pelo flask
        return {'hello': 'world by apps'}


api = Api()


def configure_api(app):

    # adicionamos a rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
