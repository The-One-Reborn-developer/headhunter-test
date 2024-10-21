from flask import Flask

from app.database.queues.create_database_tables import create_database_tables


app = Flask(__name__)


if __name__ == '__main__':
    create_database_tables()