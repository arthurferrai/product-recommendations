# coding=utf-8
from flask import Flask, request, jsonify
from model import DBModelBase


class FlaskServer(object):
    def __init__(self, model):
        # type: (DBModelBase) -> None
        self.model = model

        self.app = Flask(__name__)
        self.app.add_url_rule('/customers/', view_func=self.customers, methods=['GET', 'POST'])
        self.app.add_url_rule('/products/', view_func=self.products, methods=['GET', 'POST'])
        self.app.add_url_rule('/product-views/', view_func=self.product_views, methods=['GET', 'POST'])
        self.app.add_url_rule('/recommendations/<slug>', view_func=self.get_product_recommendations)

    def run(self):
        self.app.run()

    def customers(self):
        if request.method == 'GET':
            return jsonify(self.model.get_customers())
        elif request.method == 'POST':
            self.model.create_customer(name=request.args['name'])

    def products(self):
        if request.method == 'GET':
            return jsonify(self.model.get_products())
        elif request.method == 'POST':
            self.model.create_product(name=request.args['name'])

    def product_views(self):
        if request.method == 'GET':
            return jsonify(self.model.get_product_views())
        elif request.method == 'POST':
            self.model.create_product_view(product=request.args['product'], name=request.args['name'])

    def get_product_recommendations(self, product_slug):
        # type: (str) -> None
        self.model.get_recommendations(product_slug, int(request.args['limit']))
