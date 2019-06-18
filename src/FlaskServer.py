# coding=utf-8
import json

from flask import Flask, request, jsonify
from typing import List

from model import DBModelBase


class FlaskServer(object):
    def __init__(self, model, host, port):
        # type: (DBModelBase, str, int) -> None
        self.model = model
        self.host = host
        self.port = port

        self.app = Flask(__name__)
        self.app.add_url_rule('/customers/', view_func=self.customers, methods=['GET', 'POST'])
        self.app.add_url_rule('/products/', view_func=self.products, methods=['GET', 'POST'])
        self.app.add_url_rule('/product-views/', view_func=self.product_views, methods=['GET', 'POST'])
        self.app.add_url_rule('/recommendations/<slug>/', view_func=self.get_product_recommendations)

    def run(self):
        self.app.run(host=self.host, port=self.port)

    def customers(self):
        if request.method == 'GET':
            return jsonify(self.model.get_customers())
        elif request.method == 'POST':
            params = json.loads(request.data)
            self.model.create_customer(name=params['name'])
            return ''

    def products(self):
        if request.method == 'GET':
            return jsonify(self.model.get_products())
        elif request.method == 'POST':
            params = json.loads(request.data)
            self.model.create_product(name=params['name'])
            return ''

    def product_views(self):
        if request.method == 'GET':
            return jsonify(self.model.get_product_views())
        elif request.method == 'POST':
            params = json.loads(request.data)
            self.model.create_product_view(**params)
            return ''

    def get_product_recommendations(self, slug):
        # type: (str) -> List[dict]
        return jsonify(self.model.get_recommendations(slug, int(request.args['limit'])))
