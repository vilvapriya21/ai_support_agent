'''
memory.py
'''
class Memory:
    def __init__(self):
        self.store = {}

    def add_message(self, user_id: str, user_message: str, assistant_message: str):
        if user_id not in self.store:
            self.store[user_id] = []

        self.store[user_id].append({
            "user": user_message,
            "assistant": assistant_message
        })

    def get_last_messages(self, user_id: str, limit: int = 3):
        return self.store.get(user_id, [])[-limit:]
