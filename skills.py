from flask import Flask, request
from flask_restful import Resource, Api
import json

lista_habilidades = ['Python', 'Java', 'PHP', 'C', 'Javascript']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
