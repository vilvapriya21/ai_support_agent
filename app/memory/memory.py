class Memory:

    def __init__(self, window_size: int = 3):
        self.store = {}
        self.window_size = window_size

    def get_last_messages(self, user_id: str):
        history = self.store.get(user_id, [])
        return history[-self.window_size:]

    def add_message(self, user_id: str, user_message: str, assistant_message: str):
        if user_id not in self.store:
            self.store[user_id] = []
        self.store[user_id].append({
            "user": user_message,
            "assistant": assistant_message
        })
