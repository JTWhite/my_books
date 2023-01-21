from flask_restful import Resource

# from datetime import datetime
# from typing import Optional

# from app import db


class GetBook(Resource):
    def get(self, title):
        return {title: "Did not find any match"}


# class AddBook(db.Model):

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     title = db.Column(db.String(128))

#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"<Book {self.id}>"
