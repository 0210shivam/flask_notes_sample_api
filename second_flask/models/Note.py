from datetime import datetime


class Notes:

    def __init__(self, user_id, title, desc):
        self.user_id = user_id
        self.title = title
        self.desc = desc
        self.timestamp = datetime.now().time().strftime("%d-%m-%Y, %H:%M")
