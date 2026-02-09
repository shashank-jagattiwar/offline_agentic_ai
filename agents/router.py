from scripts.query_engine import QueryEngine


class AgentRouter:
    def __init__(self):
        self.query_engine = QueryEngine()

    def handle_query(self, question, mode):
        return self.query_engine.query(question, mode)
