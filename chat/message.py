from datetime import datetime
from json import JSONEncoder


class Message:

    def __init__(self, title: str, text: str, author: str):
        self.title = title
        self.text = text
        self.author = author
        self.date = datetime.now()


class MessageEncoder(JSONEncoder):

    def default(self, message):
        if isinstance(message, Message):
            json_res = {
                "title": message.title,
                "text": message.text,
                "author": message.author,
                "date": str(message.date)
            }
            return json_res

        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return JSONEncoder.default(self, message)
