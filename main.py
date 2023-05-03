from mod import *
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)


class StartingNewProjetFlask(Resource):
    def get(self, querystring, payload):
        projet = StartingNewProjet(querystring, payload)
        start = projet.run()
        return jsonify(start)


class ActiverAuditFlask(Resource):
    def get(self, querystring, payload, id_projet):
        active = ActiverAudit(querystring, payload, id_projet)
        start = active.run()
        return jsonify(start)


class ExecuterAuditFlask(Resource):
    def get(self, querystring, id_projet):
        execute = ExecuterAudit(querystring, id_projet)
        start = execute.run()
        return jsonify(start)


class ObtenirRapportFlask(Resource):
    def get(self, querystring, id_projet):
        obtenir = ObtenirRapport(querystring, id_projet)
        start = obtenir.run()
        return jsonify(start)


@app.route('/')
def home():
    return "SEMRUSH API RUNNING ..."


api.add_resource(StartingNewProjetFlask, '/StartingNewProjetFlask/<querystring>/<payload>')  # Route_1
api.add_resource(ActiverAuditFlask, '/ActiverAudit/<querystring>/<payload>/<id_projet>')  # Route_2
api.add_resource(ExecuterAuditFlask, '/ExecuterAuditFlask/<querystring>/<id_projet>')  # Route_3
api.add_resource(ObtenirRapportFlask, '/ObtenirRapportFlask/<querystring>/<id_projet>')  # Route_4

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999)
