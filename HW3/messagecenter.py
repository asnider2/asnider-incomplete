class Message:
    def __init__(self, from_user: str, to_user: str, contents: str):
        self.from_user = from_user
        self.to_user = to_user
        self.contents = contents
        self.read = False

        # TODO: (Part 3 of the assignment)
        # - Add a field to store the timestamp of when the message is created. (Hint: Use datetime)
        # - Add another field to store the length of the message content.
    
    def mark_read(self):
        self.read = True


class MessageCenter:
    #TODO: All of the functions (Part 2 of the assignment)

    def __init__(self):
        pass

    def add_user_to_group(self, group: str, user: str):
        pass

    def add_direct_message(self, from_user: str, to_user: str, contents: str):
        pass

    def add_group_message(self, from_user: str, group: str, contents: str):
        pass

    def next_message(self, to_user: str) -> Message:
        pass

    def message_history(self, user1: str, user2: str) -> list:
        pass
    
    def delete_account(self, user: str):
        pass
