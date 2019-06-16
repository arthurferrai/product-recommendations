import sqlite3
from typing import Optional, List

from DBModelBase import DBModelBase


class SQLiteModel(DBModelBase):
    def _run_query(self, query, *args, **kwargs):
        # type: (str, list, dict) -> Optional[list]
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, *args, **kwargs)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return map(dict, result)

    def _create_table(self):
        # type: () -> None
        self._run_query("""
            CREATE TABLE IF NOT EXISTS Customers (
               Slug INTEGER PRIMARY KEY,
               Name TEXT NOT NULL
            );""")
        self._run_query("""
            CREATE TABLE IF NOT EXISTS Products (
               Slug INTEGER PRIMARY KEY,
               Name TEXT NOT NULL
            );""")
        self._run_query("""
            CREATE TABLE IF NOT EXISTS ProductViews (
               Timestamp DATE NOT NULL,
               Product INTEGER NOT NULL,
               Customer INTEGER NOT NULL,
               FOREIGN KEY (Product) REFERENCES Products(Slug),
               FOREIGN KEY (Customer) REFERENCES Customers(Slug)
            );""")

    def __init__(self, db_file='base.db'):
        self.db_file = db_file
        self._create_table()

    def get_customers(self):
        # type: () -> List[dict]
        query = """
            SELECT 
                Slug AS slug,
                Name AS name
            FROM Customers;"""
        return self._run_query(query)

    def create_customer(self, **customer_data):
        # type: (dict) -> None
        query = """
            INSERT INTO Customers (Name) VALUES (:name);"""
        self._run_query(query, customer_data)

    def get_products(self):
        # type: () -> List[dict]
        query = """
            SELECT 
                Slug AS slug,
                Name AS name
            FROM Products;"""
        return self._run_query(query)

    def create_product(self, **product_data):
        # type: (dict) -> None
        query = """
            INSERT INTO Products (Name) VALUES (:name);"""
        self._run_query(query, product_data)

    def get_product_views(self):
        # type: () -> List[dict]
        query = """
            SELECT 
                Timestamp AS timestamp,
                Product AS product,
                Customer AS customer
            FROM ProductViews;"""
        return self._run_query(query)

    def create_product_view(self, **view_data):
        # type: (dict) -> None
        query = """
            INSERT INTO ProductViews (Timestamp, Product, Customer)
            VALUES (datetime('now'), :product, :customer);"""
        self._run_query(query, view_data)

    def get_recommendations(self, product, limit):  # type: (str, int) -> List[dict]
        query = """
            SELECT 
                Product AS product,
                COUNT(product) AS score
            FROM ProductViews
            GROUP BY Product
            ORDER BY score DESC;"""
        return self._run_query(query)
