from flask import current_app as app
from flask_restful import Api, Resource 
from flask import request
from flask import jsonify
from utils.model_predict import predict

api = Api(app)


class TraditionalMLAPI(Resource):
    def get(self):
        try:
            text = request.json["text"]
            prediction = predict(text = text, model_code = "T")
            return {"prediction": int(prediction)}
        except Exception as e:
            return {"Error": str(e)}, 422

class LSTMModelAPI(Resource):
    def get(self):
        try:
            text = request.json["text"]
            prediction = predict(text = text, model_code = "L")
            return {"prediction": int(prediction)}
        except Exception as e:
            return {"Error": str(e)}, 422

class FusionModelAPI(Resource):
    def get(self):
        return "hi"

api.add_resource(LSTMModelAPI, "/api/lstmapi")
api.add_resource(FusionModelAPI, "/api/fusionapi")
api.add_resource(TraditionalMLAPI, "/api/traditionalmlapi")



