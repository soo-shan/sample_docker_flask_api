from crypt import methods
import os
import json

from default_app import app
from flask import request, jsonify, send_file
from flask_restful import Resource, Api

from codes import pdf_to_img

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

api = Api(app)

@app.route("/", methods=["POST"])
class PdfConverter(Resource):

    def post(self):
        id = request.form.get("id", None)
        doc_name = request.form.get("doc_name", None)

        if id is None:
            return {"msg":"id not Found", "status":"Failure"}, 400
        
        if doc_name is None:
            return {"msg":"doc_name not Found", "status":"Failure"}, 400
        
        file_data = request.files.get("binary_pdf")
        
        response = pdf_to_img.pdf2img(file_data)

        return response
    
api.add_resource(PdfConverter, "/app/pdfconverter")

    