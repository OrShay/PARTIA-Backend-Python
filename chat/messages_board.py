import json

from chat.message import Message, MessageEncoder


class MessagesBoard:

    def __init__(self):
        self.messages = []

    def add_message(self, title, text, author):
        new_message = Message(title, text, author)
        self.messages.append(new_message)

    def get_all_messages(self):
        messages_list = [json.loads(MessageEncoder().encode(message)) for message in self.messages]
        return messages_list
