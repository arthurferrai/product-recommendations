from typing import List


class DBModelBase(object):
    def __init__(self):
        raise NotImplemented()

    def get_customers(self):
        # type: () -> List[dict]
        raise NotImplemented()

    def create_customer(self, **customer_data):
        # type: (dict) -> None
        raise NotImplemented()

    def get_products(self):
        # type: () -> List[dict]
        raise NotImplemented()

    def create_product(self, **product_data):
        # type: (dict) -> None
        raise NotImplemented()

    def get_product_views(self):
        # type: () -> List[dict]
        raise NotImplemented()

    def create_product_view(self, **view_data):
        # type: (dict) -> None
        raise NotImplemented()

    def get_recommendations(self, product, limit):
        # type: (str, int) -> List[dict]
        raise NotImplemented()
