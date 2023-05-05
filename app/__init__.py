"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaak83hp8u791gupogg-a",
        database="todo_1bho",
        user="todo_1bho_user",
        password="kKhIr2wiQBbQZNcPeyD6ksSGAtLYESkb")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
