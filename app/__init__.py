"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12ro8rddl13a53d190-a.oregon-postgres.render.com",
        database="todo_l4cf",
        user="todo_l4cf",
        password="JiPFT6B6ksUPNoEbB55hKQwxExBnmOWN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
