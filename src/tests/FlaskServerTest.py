from unittest import TestCase
from mock import Mock

from src.FlaskServer import FlaskServer
from src.model import DBModelBase


class MockupModel(DBModelBase):
    # noinspection PyMissingConstructor
    def __init__(self):
        self.get_products = Mock(return_value={})
        self.create_product = Mock()
        self.get_customers = Mock(return_value={})
        self.create_customer = Mock()
        self.get_product_views = Mock(return_value={})
        self.create_product_view = Mock()
        self.get_recommendations = Mock(return_value={})


class FlaskServerTest(TestCase):
    def setUp(self):
        self.model = MockupModel()
        self.server = FlaskServer(self.model, '127.0.0.1', '9999')
        self.server.app.config['TESTING'] = True

    def test_get_products(self):
        with self.server.app.test_client() as c:
            c.get('/products/')
        self.assertTrue(self.model.get_products.called)

    def test_create_product(self):
        with self.server.app.test_client() as c:
            c.post('/products/', data='{"name": "Product 1"}')
        self.assertTrue(self.model.create_product.called)

    def test_get_customers(self):
        with self.server.app.test_client() as c:
            c.get('/customers/')
        self.assertTrue(self.model.get_customers.called)

    def test_create_customer(self):
        with self.server.app.test_client() as c:
            c.post('/customers/', data='{"name": "Customer 1"}')
        self.assertTrue(self.model.create_customer.called)

    def test_get_product_views(self):
        with self.server.app.test_client() as c:
            c.get('/product-views/')
        self.assertTrue(self.model.get_product_views.called)

    def test_create_product_view(self):
        with self.server.app.test_client() as c:
            c.post('/product-views/', data='{"product": 1, "customer": 1}')
        self.assertTrue(self.model.create_product_view.called)

    def test_get_recommendation(self):
        with self.server.app.test_client() as c:
            c.get('/recommendations/1/?limit=1')
        self.assertTrue(self.model.get_recommendations.called)
